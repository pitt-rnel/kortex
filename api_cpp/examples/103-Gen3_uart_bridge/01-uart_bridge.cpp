/*
* KINOVA (R) KORTEX (TM)
*
* Copyright (c) 2019 Kinova inc. All rights reserved.
*
* This software may be modified and distributed
* under the terms of the BSD 3-Clause license.
*
* Refer to the LICENSE file for details.
*
*/

/*
* 103-Gen3_uart_bridge/uart_bridge.cpp
*
* Usage example for the UART Expansion IO on the Gen3 Interconnect module.
*
* PHYSICAL SETUP:
* =========
* For this example to work, you will have to connect the RX and TX pins on the interconnect 
* IO Expansion pinout, so that the TX is transmitted right into the RX.
*
* DESCRIPTION OF CURRENT EXAMPLE:
* ===============================
* In this example, the UART bridge class encapsulates all necessary Kortex API
* objects and implements the functions to setup the UART, write to the bus and read back from it.
* 
* The Init function creates the Kortex API objects, connects to the arm and also calls InitSocket, 
* which correctly configures the socket (depending if you are on Windows or Linux).
*
* The Run function :
*   - Tells the Interconnect (m_interconnect_config object) to enable the UART bridge (this is where you supply the UART parameters)
*   - Tells the Base (m_base) to enable the UART bridge
*   - Opens the TCP socket to the base and writes the test string to the UART bridge
*   - Waits 10 seconds and prints every character it receives
*   - Tells the Base (m_base) to disable the UART bridge
*   - Tells the Interconenct (m_interconnect_config_object) to disable the UART bridge
*/

#include <BaseClientRpc.h>
#include <InterconnectConfigClientRpc.h>
#include <SessionManager.h>
#include <DeviceManagerClientRpc.h>
#include <RouterClient.h>
#include <TransportClientTcp.h>

#ifdef _WIN32
/* See http://stackoverflow.com/questions/12765743/getaddrinfo-on-win32 */
#include <winsock2.h>
#include <Ws2tcpip.h>
#else
/* Assume that any non-Windows platform uses POSIX-style sockets instead. */
#include <sys/time.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#define SOCKET int
#endif

#include <stdio.h>
#include <string.h>
#include <chrono>
#include <math.h>

namespace k_api = Kinova::Api;

#define IP_ADDRESS "192.168.110.11"
#define PORT 10000

///////////////////////////////////////////////////////////////////////
// class UARTBridge
//
// Implements methods for establishing and operating UART bridge through
// the base.
///////////////////////////////////////////////////////////////////////
class UARTBridge
{
public:
    UARTBridge(const std::string& ip_address, int port, const std::string& username = "admin", const std::string& password = "admin"):
    m_ip_address(ip_address), m_username(username), m_password(password), m_port(port), m_interconnect_device_id(0)
    {
        m_router              = nullptr;
        m_transport           = nullptr;
        m_session_manager     = nullptr;
        m_base                = nullptr;
        m_device_manager      = nullptr;
        m_interconnect_config = nullptr;
    }

    ~UARTBridge()
    {
        // Close API session
        m_session_manager->CloseSession();

        // Deactivate the router and cleanly disconnect from the transport object
        m_router->SetActivationStatus(false);
        m_transport->disconnect();

        // Destroy the API
        delete m_interconnect_config;
        delete m_device_manager;
        delete m_session_manager;
      	delete m_base;
        delete m_router;
        delete m_transport;
    }

    void Init()
    {
        m_transport = new k_api::TransportClientTcp();
        m_transport->connect(m_ip_address, m_port);
        m_router = new k_api::RouterClient(m_transport, [](k_api::KError err){ std::cout << "_________ callback error _________" << err.toString(); });
        
        // Set session data connection information
        auto createSessionInfo = k_api::Session::CreateSessionInfo();
        createSessionInfo.set_username(m_username);
        createSessionInfo.set_password(m_password);
        createSessionInfo.set_session_inactivity_timeout(60000);   // (milliseconds)
        createSessionInfo.set_connection_inactivity_timeout(2000); // (milliseconds)

        // Session manager service wrapper
        m_session_manager = new k_api::SessionManager(m_router);
        m_session_manager->CreateSession(createSessionInfo);

        // Create services
        m_device_manager = new k_api::DeviceManager::DeviceManagerClient(m_router);
        m_interconnect_config = new k_api::InterconnectConfig::InterconnectConfigClient(m_router);
        m_base = new k_api::Base::BaseClient(m_router);

        m_interconnect_device_id = GetDeviceIdFromDevType(k_api::Common::INTERCONNECT, 0);
    
        InitSocket();
    }

    uint32_t GetDeviceIdFromDevType(k_api::Common::DeviceTypes device_type, uint32_t device_index)
    {
        auto device_handles = m_device_manager->ReadAllDevices();
        uint32_t current_index = 0;
        for (auto device_handle : device_handles.device_handle() )
        {
            if (device_handle.device_type() == device_type)
            {
                if (current_index == device_index)
                {
                    return device_handle.device_identifier();
                }
                ++current_index;
            }
        }
        return 0;
    }

    void Run()
    {
        const char test_string[] = "abcdefghijklmnopqrsuvwxyz\n";
        char buffer[128] = { 0 };

        if (m_interconnect_device_id == 0)
        {
            std::cout << "Error : No interconnect found!" << std::endl;
            return;
        }
        std::cout << "Interconnect ID found = " <<  m_interconnect_config  << std::endl;

        ///////////////////////////////////////////////////////////////////////
        // Enable and configure UART on interconnect
        ///////////////////////////////////////////////////////////////////////

        k_api::Common::UARTConfiguration uart_config;
        uart_config.set_port_id(k_api::InterconnectConfig::UART_PORT_EXPANSION);
        uart_config.set_enabled(true);   // Setting enabled to true opens the tcp port dedicated to UART bridging. Setting this
                                        // field to false disables designated uart and closes the TCP port.

        uart_config.set_speed(k_api::Common::UART_SPEED_115200);
        uart_config.set_word_length(k_api::Common::UART_WORD_LENGTH_8);
        uart_config.set_stop_bits(k_api::Common::UART_STOP_BITS_1);
        uart_config.set_parity(k_api::Common::UART_PARITY_NONE);
        m_interconnect_config->SetUARTConfiguration(uart_config, m_interconnect_device_id);

        ///////////////////////////////////////////////////////////////////////
        // Enable port bridging on the base
        ///////////////////////////////////////////////////////////////////////

        k_api::Base::BridgeConfig bridge_config;
        bridge_config.set_device_identifier(m_interconnect_device_id);
        bridge_config.set_bridgetype(k_api::Base::BRIDGE_TYPE_UART);
        auto bridge_result = m_base->EnableBridge(bridge_config);
        if (bridge_result.status() != k_api::Base::BRIDGE_STATUS_OK) 
        {
            return;
        }

        ///////////////////////////////////////////////////////////////////////
        // Get the bridge config and print it
        ///////////////////////////////////////////////////////////////////////

        uint32_t bridge_id = bridge_result.bridge_id().bridge_id();
        k_api::Base::BridgeIdentifier bridge_identifier;
        bridge_identifier.set_bridge_id(bridge_id);
        bridge_config = m_base->GetBridgeConfig(bridge_identifier);

        uint16_t base_port           = (uint16_t) bridge_config.port_config().out_port();
        uint16_t interconnect_port   = (uint16_t) bridge_config.port_config().target_port();

        std::cout << "Bridge ID# " << bridge_id <<" created between Interconnect (dev#" << m_interconnect_device_id << ")";
        std::cout << " port #" << interconnect_port << " and external port #"<< base_port << std::endl;

        ///////////////////////////////////////////////////////////////////////
        // Open TCP socket to bridge port and send sample data through socket
        ///////////////////////////////////////////////////////////////////////
        
        int num_packets = 1000; // Number of test packets to send
        int packets_sent = 1;

        // Initialize some vars for calculating timing stats
        int i = 0;
        double t[100] = { 0 };
        double sum = 0.0;
        double tmin = 0.0;
        double tmax = 0.0;
        double avg = 0.0;
        double sse = 0.0;
        double stdev = 0.0;
        int bytes_sent = 0;
        int bytes_read = 0;

        SOCKET uart_socket = ConnectSocket(IP_ADDRESS, base_port);
        if (uart_socket < 0)
        {
            std::cout << "Socket Connect failed\n";
            return;
        }

        for (; packets_sent <= num_packets; packets_sent++) {
            // Mark the send time of packet
            std::chrono::time_point<std::chrono::steady_clock> tx_timestamp = chrono::steady_clock::now();

            // Send data through the bridge
            bytes_sent = send(uart_socket, test_string, sizeof(test_string), 0);
            if (bytes_sent != sizeof(test_string)) {
                fprintf(stderr, "Did not send the full test string. %d of %zu\n", bytes_sent, sizeof(test_string));
                return;
            }

            // Block waiting for data to echo back
            bytes_read = recv(uart_socket, buffer, sizeof(test_string), MSG_WAITALL);
            if (bytes_read != bytes_sent) {
                fprintf(stderr, "Wrong number of bytes received. %d of %d\n", bytes_read, bytes_sent);
                return;

            }

            // Mark the receive time of the reply
            std::chrono::time_point<std::chrono::steady_clock> rx_timestamp = chrono::steady_clock::now();

            // Calculate the roundtrip time and store the time
            std::chrono::duration<double> dt = rx_timestamp - tx_timestamp;
            t[i] = dt.count();
            i++;

            // Check the reply
            if (strcmp(test_string, buffer) != 0) {
                fprintf(stderr, "Reply was invalid: %s\n", buffer);
                return;
            }

            // Print stats every 100 packets
            if ((i % 100) == 0) {
                sum = 0.0;
                stdev = 0.0;
                avg = 0.0;
                tmin = 100.0;
                tmax = 0.0;
                sse = 0.0;

                // Calculate average and range
                for (int n = 0; n < 100; n++) {
                    // Aggregate sum
                    sum = sum + t[n];

                    // Store min
                    if (t[n] < tmin) {
                        tmin = t[n];
                    }

                    // Store max
                    if (t[n] > tmax) {
                        tmax = t[n];
                    }
                }
                
                avg = sum / 100.0;
                
                // Calculate standard deviation
                for (int n = 0; n < 100; n++) {
                    sse = sse + pow(t[n] - avg, 2);
                }
                stdev = sqrt(sse / 100.0);

                // Print packet timing info
                printf("[%05d]:  %0.6f +/- %0.6f [%0.6f to %0.6f] secs\n", packets_sent, avg, stdev, tmin, tmax);

                // Reset counter
                i = 0;
            }
        }

        std::cout << std::endl;

        std::cout << "Test over!" << std::endl;

        ///////////////////////////////////////////////////////////////////////
        // Close TCP connection and disable bridge on interconnect and base
        ///////////////////////////////////////////////////////////////////////

        CloseSocket(uart_socket);
        
        // Disable bridge on Base
        bridge_identifier.set_bridge_id(bridge_id);
        m_base->DisableBridge(bridge_identifier);

        // Disable UART bridge on Interconnect
        uart_config.set_enabled(false);
        m_interconnect_config->SetUARTConfiguration(uart_config, m_interconnect_device_id);

        QuitSocket();
    }

private:
    k_api::RouterClient*                                 m_router;
    k_api::TransportClientTcp*                           m_transport;
    k_api::SessionManager*                               m_session_manager;
    k_api::Base::BaseClient*                             m_base;
    k_api::DeviceManager::DeviceManagerClient*           m_device_manager;
    k_api::InterconnectConfig::InterconnectConfigClient* m_interconnect_config;

    std::string m_username;
    std::string m_password;
    std::string m_ip_address;
    int         m_port;
    uint32_t    m_interconnect_device_id;

    // Private methods
    int InitSocket(void)
    {
#ifdef _WIN32
        WSADATA wsa_data;
        return WSAStartup(MAKEWORD(1,1), &wsa_data);
#else
        return 0;
#endif
    }

    int QuitSocket(void)
    {
#ifdef _WIN32
        return WSACleanup();
#else
        return 0;
#endif
    }

    int CloseSocket(SOCKET sock)
    {
        int status = 0;
#ifdef _WIN32
        status = shutdown(sock, SD_BOTH);
        if (status == 0)
        {
            status = closesocket(sock);
        }
#else
        status = shutdown(sock, SHUT_RDWR);
        if (status == 0)
        {
            status = close(sock);
        }
#endif
        return status;
    }

    SOCKET ConnectSocket(const char* ip_address, int port)
    {
        SOCKET sock;
        struct sockaddr_in server;
        //Create socket
        sock = socket(AF_INET , SOCK_STREAM , 0);
        if (sock < 0)
        {
            return -1;
        }

        server.sin_addr.s_addr = inet_addr(ip_address);
        server.sin_family = AF_INET;
        server.sin_port = htons(port);
        if (connect(sock , (struct sockaddr *)&server , sizeof(server)) < 0)
        {
            std::cout << "Connect failed." << std::endl;
            return -1;
        }
        return sock;
    }
};

// Example core
// Implements a sample UART bridge application.
int main(int argc, char **argv)
{
    UARTBridge* uart_bridge;
    uart_bridge = new UARTBridge(IP_ADDRESS, PORT, "rnel", "monkeydew");
    uart_bridge->Init();
    uart_bridge->Run();

    delete uart_bridge;

    return 0;
};
