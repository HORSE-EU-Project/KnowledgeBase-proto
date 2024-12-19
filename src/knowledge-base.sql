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
1	ntp_dos
2	pfcf_dos
3	dns_reflection_amplification
\.


--
-- Data for Name: attacks_mitigations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.attacks_mitigations (id, attack, mitigation, mitigation_priority, description) FROM stdin;
1	ntp_dos	monlist_disable	3	Disabling the 'monlist' command, which is known to be exploited in NTP-based DoS attacks, directly addresses a specific vulnerability. This reduces the attack surface and prevents attackers from exploiting this particular feature.
2	ntp_dos	absorb_traffic	2	Absorbing and redirecting malicious traffic through anycast blackholing helps to mitigate the attack by preventing the malicious traffic from reaching its target. This keeps the network stable and buys time for implementing longer-term solutions.
3	ntp_dos	ntp_service_switch_off	1	Temporarily shutting down the NTP service is the fastest way to halt the attack's impact and prevent further disruption while other measures are implemented. This minimizes immediate network instability and allows time for a strategic response.
4	ntp_dos	server_handover	4	Handover to a backup server or a more secure server setup can ensure continuity of service while the primary server is being secured and analyzed. This provides a resilient operational backup and minimizes downtime for critical services.
5	ntp_dos	investigations_report	7	Conducting thorough investigations and reporting on the attack is essential for understanding the attack's nature, origin, and impact. This information is vital for preventing future incidents, improving defenses, and potentially taking legal or corrective actions against the attackers.
6	ntp_dos	firewall_spoofing_detection	5	Implementing firewall rules to detect and block spoofed traffic can significantly reduce the volume of attack traffic, thereby protecting the network from further DoS attempts. This is a crucial step in mitigating ongoing threats and enhancing network security.
7	ntp_dos	upgrade_software	6	Upgrading NTP to a version higher than 4.7.2 ensures that the system is not vulnerable to known exploits that have been patched in later versions. This long-term measure enhances overall security and prevents similar attacks in the future.
14	pfcf_dos	sba_function_disable	1	Temporarily disabling the affected Service-Based Architecture (SBA) function can immediately halt the attack’s impact on the PFCF, preventing further degradation of network services. This is a quick and effective way to contain the attack and stabilize the network, allowing time for implementing additional mitigations.
8	dns_reflection_amplification	dns_service_disable	1	Temporarily disabling the DNS service immediately halts the attack's impact, preventing further disruption to network services. This drastic measure provides immediate relief, allowing time to implement other mitigation strategies without the attack continuously degrading service quality.
17	pfcf_dos	rate_limiting	2	Implementing rate limiting controls the flow of traffic to the PFCF, preventing excessive requests from overwhelming the system. This helps to mitigate the ongoing attack by managing the load on the PFCF, ensuring it can handle legitimate traffic while the attack is being addressed.
16	pfcf_dos	investigation_report	4	Conducting thorough investigations and compiling reports on the attack provides valuable insights into its nature, origin, and impact. Understanding the attack is crucial for improving defenses, preventing future incidents, and potentially taking legal or corrective actions against the attackers. This step, while essential, is prioritized after immediate containment and mitigation measures.
15	pfcf_dos	new_ns_slice_creation	3	Creating a new Network Slice (NS) provides an isolated environment for critical services, ensuring they remain operational even if the primary slice is under attack. This action enhances network resilience and allows for continued service delivery to essential functions while the primary slice is secured and analyzed.
13	dns_reflection_amplification	anycast_blackhole	2	Utilizing anycast blackholing to absorb and redirect malicious traffic prevents the harmful traffic from overwhelming the DNS servers. This approach helps maintain network stability and minimizes the impact on legitimate users.
10	dns_reflection_amplification	dns_firewall_spoofing_detection	5	Configuring firewalls to detect and block spoofed traffic helps reduce the volume of attack traffic by filtering out illegitimate requests. This defensive measure enhances network security and aids in mitigating ongoing attacks.
9	dns_reflection_amplification	dns_rate_limiting	3	Implementing rate limiting controls the flow of traffic to the DNS servers, mitigating the attack by preventing excessive requests from overloading the system. This action helps preserve server performance and maintains service availability for legitimate traffic.
12	dns_reflection_amplification	dns_service_handover	4	Handover to a backup or more secure DNS server ensures continuity of service while the primary server is secured and analyzed. This action provides operational resilience and minimizes downtime for critical services, ensuring that DNS resolution remains functional.
\.


--
-- Data for Name: mitigation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mitigation (id, name, field_name, field_value) FROM stdin;
1	monlist_disable	\N	\N
2	upgrade_software	\N	\N
3	firewall_spoofing_detection	\N	\N
4	investigations_report	\N	\N
5	server_handover	\N	\N
6	ntp_service_switch_off	\N	\N
8	dns_service_disable	\N	\N
10	sba_function_disable	\N	\N
11	new_ns_slice_creation	\N	\N
12	rate_limiting	\N	\N
7	anycast_blackhole	\N	\N
13	dns_service_handover	\N	\N
9	dns_rate_limiting	rate	\N
14	dns_firewall_spoofing_detection	interface	\N
15	dns_firewall_spoofing_detection	destination_host	\N
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

