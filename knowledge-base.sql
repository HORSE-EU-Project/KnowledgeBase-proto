--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2 (Debian 16.2-1.pgdg120+2)
-- Dumped by pg_dump version 16.2 (Debian 16.2-1.pgdg120+2)

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
    name character varying(255),
    description character varying(255),
    parent_id character varying(255),
    mitigation character varying
);


ALTER TABLE public.attack OWNER TO postgres;

--
-- Name: mitigation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mitigation (
    id integer NOT NULL,
    name character varying(255),
    description character varying(255),
    playbook_endpoint character varying(255)
);


ALTER TABLE public.mitigation OWNER TO postgres;

--
-- Data for Name: attack; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.attack (id, name, description, parent_id, mitigation) FROM stdin;
123	DoS	denial of service attack	None	filter_network_traffic
666	Data Manipulation	manipulate data to influence external outcomes	None	network_segmentation
999	denial of service	Adversaries may perform Endpoint Denial of Service DoS attacks to degrade or block the availability of services to users	\N	filter_network_traffic
1	ntp_dos	\N	\N	monlist_disable
2	ntp_dos	\N	\N	absorb_traffic
3	ntp_dos	\N	\N	ntp_service_switch_off
4	ntp_dos	\N	\N	server_handover
5	ntp_dos	\N	\N	investigations_report
6	ntp_dos	\N	\N	firewall_spoofing_detection
7	ntp_dos	\N	\N	upgrade_software
14	pfcf_dos	\N	\N	sba_function_table
13	dns_reflection_amplification	\N	\N	absorb_traffic
11	dns_reflection_amplification	\N	\N	investigation_report\n
10	dns_reflection_amplification	\N	\N	firewall_spoofing_detection
9	dns_reflection_amplification	\N	\N	rate_limiting
8	dns_reflection_amplification	\N	\N	dns_service_disable
17	pfcf_dos	\N	\N	rate_limiting
16	pfcf_dos	\N	\N	investigation_report
15	pfcf_dos	\N	\N	new_ns_slice_creation
12	dns_reflection_amplification	\N	\N	server_handover
\.


--
-- Data for Name: mitigation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mitigation (id, name, description, playbook_endpoint) FROM stdin;
222	network_segmentation	Identify critical business and system processes that may be targeted by adversaries and work to isolate and secure those systems against unauthorized access and tampering.	https://github.com/martel-innovate/horse.rtr/blob/main/api-test/iptables.yaml
111	filter_network_traffic	Filter traffic on port 80	https://github.com/martel-innovate/horse.rtr/blob/main/api-test/docker-compose/ansible-rules/netfilter.yaml
1	monlist_disable	\N	\N
2	upgrade_software	\N	\N
3	firewall_spoofing_detection	\N	\N
4	investigations_report	\N	\N
5	server_handover	\N	\N
6	ntp_service_switch_off	\N	\N
7	absorb_traffic	\N	\N
8	dns_service_disable	\N	\N
9	rate_limiting	\N	\N
10	sba_function_disable	\N	\N
11	new_ns_slice_creation	\N	\N
\.


--
-- Name: attack attack_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attack
    ADD CONSTRAINT attack_pkey PRIMARY KEY (id);


--
-- Name: mitigation mitigation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mitigation
    ADD CONSTRAINT mitigation_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

