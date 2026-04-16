from collections import defaultdict

FILE_NAME = "logs.txt"

fail_users = defaultdict(int)
ip_attacks = defaultdict(int)
total_lines = 0

print("🔍 Loading logs...\n")

try:
    with open(FILE_NAME, "r") as file:
        for line in file:
            total_lines += 1
            parts = line.strip().split()

            if len(parts) < 4:
                continue

            timestamp = parts[0] + " " + parts[1]
            event = parts[2]
            user = parts[3]
            ip = parts[4]

            if event == "LOGIN_FAIL":
                fail_users[user] += 1
                ip_attacks[ip] += 1

except FileNotFoundError:
    print("❌ File not found! Make sure logs.txt exists.")
    exit()

print("🚨 SECURITY REPORT\n")
print(f"Total log entries: {total_lines}\n")

# أكثر المستخدمين فشل
print("👤 Suspicious Users:")
found = False
for user, count in fail_users.items():
    if count >= 3:
        print(f"- {user}: {count} failed attempts ⚠️")
        found = True

if not found:
    print("- No suspicious users found")

# أكثر IP هجوم
print("\n🌐 Suspicious IPs:")
found = False
for ip, count in ip_attacks.items():
    if count >= 3:
        print(f"- {ip}: {count} failed attempts 🔥")
        found = True

if not found:
    print("- No suspicious IPs found")

print("\n✅ Analysis completed.")
