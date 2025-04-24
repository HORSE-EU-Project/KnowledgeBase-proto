--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3 (Debian 16.3-1.pgdg120+1)
-- Dumped by pg_dump version 16.3 (Debian 16.3-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: attack; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.attack (
    id integer NOT NULL,
    name character varying
);


ALTER TABLE public.attack OWNER TO postgres;

--
-- Name: attacks_mitigations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.attacks_mitigations (
    id integer NOT NULL,
    attack character varying(255),
    mitigation character varying,
    mitigation_priority integer,
    description character varying
);


ALTER TABLE public.attacks_mitigations OWNER TO postgres;

--
-- Name: mitigation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mitigation (
    id integer NOT NULL,
    name character varying(255),
    field_name character varying,
    field_value character varying
);


ALTER TABLE public.mitigation OWNER TO postgres;

--
-- Data for Name: attack; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.attack (id, name) FROM stdin;
100	ntp_dos
200	pfcf_dos
300	dns_reflection_amplification
0	hello_world
1	ddos_amplification
2	dns_amplification
3	ddos_download_link
4	data_poisoning
5	multidomain
6	mitm
7	nf_exposure
8	signaling_pfcp
9	poisoning_and_amplification
10	network_exposure
\.


--
-- Data for Name: attacks_mitigations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.attacks_mitigations (id, attack, mitigation, mitigation_priority, description) FROM stdin;
100	ntp_dos	monlist_disable	3	Disabling the 'monlist' command, which is known to be exploited in NTP-based DoS attacks, directly addresses a specific vulnerability. This reduces the attack surface and prevents attackers from exploiting this particular feature.
200	ntp_dos	absorb_traffic	2	Absorbing and redirecting malicious traffic through anycast blackholing helps to mitigate the attack by preventing the malicious traffic from reaching its target. This keeps the network stable and buys time for implementing longer-term solutions.
300	ntp_dos	ntp_service_switch_off	1	Temporarily shutting down the NTP service is the fastest way to halt the attack's impact and prevent further disruption while other measures are implemented. This minimizes immediate network instability and allows time for a strategic response.
400	ntp_dos	server_handover	4	Handover to a backup server or a more secure server setup can ensure continuity of service while the primary server is being secured and analyzed. This provides a resilient operational backup and minimizes downtime for critical services.
500	ntp_dos	investigations_report	7	Conducting thorough investigations and reporting on the attack is essential for understanding the attack's nature, origin, and impact. This information is vital for preventing future incidents, improving defenses, and potentially taking legal or corrective actions against the attackers.
600	ntp_dos	firewall_spoofing_detection	5	Implementing firewall rules to detect and block spoofed traffic can significantly reduce the volume of attack traffic, thereby protecting the network from further DoS attempts. This is a crucial step in mitigating ongoing threats and enhancing network security.
700	ntp_dos	upgrade_software	6	Upgrading NTP to a version higher than 4.7.2 ensures that the system is not vulnerable to known exploits that have been patched in later versions. This long-term measure enhances overall security and prevents similar attacks in the future.
1	hello_world	execute_test_1	1	Ensures that the specified test sequence operates correctly across various modules involved in data ingestion, enrichment, and threat recognition.
82	signaling_pfcp	validate_smf_integrity	2	Detects alterations in a key network function and restores safe operational state if tampering is found.
91	poisoning_and_amplification	discard_unauthorized_packets	1	Filters and discards packets that lack authorization to prevent both internal compromise and resource misuse from external spoofing attempts.
800	dns_reflection_amplification	dns_service_disable	1	Temporarily disabling the DNS service immediately halts the attack's impact, preventing further disruption to network services. This drastic measure provides immediate relief, allowing time to implement other mitigation strategies without the attack continuously degrading service quality.
900	dns_reflection_amplification	dns_rate_limiting	3	Implementing rate limiting controls the flow of traffic to the DNS servers, mitigating the attack by preventing excessive requests from overloading the system. This action helps preserve server performance and maintains service availability for legitimate traffic.
101	dns_reflection_amplification	dns_firewall_spoofing_detection	5	Configuring firewalls to detect and block spoofed traffic helps reduce the volume of attack traffic by filtering out illegitimate requests. This defensive measure enhances network security and aids in mitigating ongoing attacks.
121	dns_reflection_amplification	dns_service_handover	4	Handover to a backup or more secure DNS server ensures continuity of service while the primary server is secured and analyzed. This action provides operational resilience and minimizes downtime for critical services, ensuring that DNS resolution remains functional.
131	dns_reflection_amplification	anycast_blackhole	2	Utilizing anycast blackholing to absorb and redirect malicious traffic prevents the harmful traffic from overwhelming the DNS servers. This approach helps maintain network stability and minimizes the impact on legitimate users.
141	pfcf_dos	sba_function_disable	1	Temporarily disabling the affected Service-Based Architecture (SBA) function can immediately halt the attack’s impact on the PFCF, preventing further degradation of network services. This is a quick and effective way to contain the attack and stabilize the network, allowing time for implementing additional mitigations.
151	pfcf_dos	new_ns_slice_creation	3	Creating a new Network Slice (NS) provides an isolated environment for critical services, ensuring they remain operational even if the primary slice is under attack. This action enhances network resilience and allows for continued service delivery to essential functions while the primary slice is secured and analyzed.
161	pfcf_dos	investigation_report	4	Conducting thorough investigations and compiling reports on the attack provides valuable insights into its nature, origin, and impact. Understanding the attack is crucial for improving defenses, preventing future incidents, and potentially taking legal or corrective actions against the attackers. This step, while essential, is prioritized after immediate containment and mitigation measures.
171	pfcf_dos	rate_limiting	2	Implementing rate limiting controls the flow of traffic to the PFCF, preventing excessive requests from overwhelming the system. This helps to mitigate the ongoing attack by managing the load on the PFCF, ensuring it can handle legitimate traffic while the attack is being addressed.
22	dns_amplification	router_rate_limiting	2	Applies global limits at the routing layer, reducing overall traffic pressure from distributed attack sources.
61	mitm	none	0	none
99	network_exposure	none	0	none
2	hello_world	execute_test_2	2	Expands on the testing scope by including additional analysis and prediction steps to validate the behavior of detection logic across more detailed functional modules.
11	ddos_amplification	udp_traffic_filter	1	Filters targeted traffic by protocol and port, reducing the risk of resource exhaustion from spoofed requests.
12	ddos_amplification	ntp_access_control	2	Restricts service access to known and trusted entities, minimizing the potential misuse of exposed functionalities.
21	dns_amplification	dns_rate_limiting	1	Controls the rate of incoming queries, preventing attackers from exploiting recursive responses for bandwidth exhaustion.
23	dns_amplification	block_ip_addresses	3	Eliminates known sources of malicious behavior to prevent repeated exploitation and spread.
31	ddos_download_link	dns_rate_limiting	1	Manages incoming query bursts to avoid overloading the service and downstream links.
32	ddos_download_link	router_rate_limiting	2	Implements device-level controls to absorb or redirect excessive load from compromised endpoints.
33	ddos_download_link	block_ip_addresses	3	Blocks malicious origins from repeatedly targeting the service distribution mechanism.
41	data_poisoning	data_reset_request	1	Regularly clears and refreshes input from a critical component, reducing the likelihood of corrupted influence.
42	data_poisoning	data_verification_request	2	Re-runs integrity checks to detect tampered or injected information before further processing.
51	multidomain	block_ues_multidomain	1	Restricts entities from multiple domains when suspicious patterns emerge, avoiding cascading threats across interconnected regions.
52	multidomain	define_dns_servers	2	Explicitly defines trusted name resolution paths, minimizing dependency on potentially untrusted sources.
71	nf_exposure	filter_malicious_access	1	Immediately reacts to interactions flagged as hostile to reduce unauthorized data flow or probing.
72	nf_exposure	api_rate_limiting	2	Limits the frequency of requests, protecting exposed APIs from enumeration or brute-force misuse.
81	signaling_pfcp	firewall_pfcp_requests	1	Drops risky signaling actions based on their type and volume to prevent abuse of control plane logic.
\.


--
-- Data for Name: mitigation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mitigation (id, name, field_name, field_value) FROM stdin;
100	monlist_disable	\N	\N
200	upgrade_software	\N	\N
300	firewall_spoofing_detection	\N	\N
400	investigations_report	\N	\N
500	server_handover	\N	\N
600	ntp_service_switch_off	\N	\N
700	anycast_blackhole	\N	\N
800	dns_service_disable	\N	\N
101	sba_function_disable	\N	\N
111	new_ns_slice_creation	\N	\N
121	rate_limiting	\N	\N
131	dns_service_handover	\N	\N
141	dns_firewall_spoofing_detection	interface	\N
151	dns_firewall_spoofing_detection	destination_host	\N
1	execute_test_1	test_id	\N
2	execute_test_2	test_id	\N
10	execute_test_1	modules	\N
20	execute_test_2	modules	\N
112	udp_traffic_filter	destination_port	\N
120	ntp_access_control	mode	\N
110	udp_traffic_filter	source_ip_filter	\N
11	udp_traffic_filter	protocol	\N
12	ntp_access_control	authorized_hosts	\N
220	router_rate_limiting	rate	\N
23	block_ip_addresses	blocked_ips	\N
211	dns_rate_limiting	source_ip_filter	\N
21	dns_rate_limiting	rate	\N
210	dns_rate_limiting	duration	\N
22	router_rate_limiting	device	\N
221	router_rate_limiting	duration	\N
41	data_reset_request	target_module	\N
420	data_verification_request	verification_mode	\N
51	block_ues_multidomain	domains	\N
52	define_dns_servers	dns_servers	\N
410	data_reset_request	reset_interval	\N
42	data_verification_request	target_module	\N
510	block_ues_multidomain	rate_limiting	\N
71	filter_malicious_access	actor	\N
72	api_rate_limiting	limit	\N
810	firewall_pfcp_requests	request_types	\N
820	validate_smf_integrity	action	\N
910	discard_unauthorized_packets	alarm	\N
710	filter_malicious_access	response	\N
81	firewall_pfcp_requests	drop_percentage	\N
82	validate_smf_integrity	check	\N
91	discard_unauthorized_packets	filter	\N
\.


--
-- Name: attacks_mitigations attack_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attacks_mitigations
    ADD CONSTRAINT attack_pkey PRIMARY KEY (id);


--
-- Name: attack attack_pkey1; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attack
    ADD CONSTRAINT attack_pkey1 PRIMARY KEY (id);


--
-- Name: mitigation mitigation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mitigation
    ADD CONSTRAINT mitigation_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

