#!/usr/bin/env python3
import os
import subprocess
import sys
import time

BANNER = r"""
───────────────────────────────────────────
🔥 LUMEN GIT PUSHER 1.0
🐺 Automatyczny uploader repo → GitHub
───────────────────────────────────────────
"""

print(BANNER)

# -------------------------------------
# 1. SPRAWDZENIE, CZY GIT ISTNIEJE
# -------------------------------------
def check_git():
    try:
        subprocess.check_output(["git", "--version"])
        return True
    except:
        return False


if not check_git():
    print("❌ Git nie jest zainstalowany.\n")
    print("💡 W Termux zainstaluj:")
    print("    pkg install git\n")
    sys.exit(1)

print("✔ Git znaleziony.")


# -------------------------------------
# 2. SPRAWDZENIE, CZY JESTEŚ W KATALOGU
# -------------------------------------
current = os.getcwd()
print(f"📂 Aktualny katalog: {current}")

if ".git" in os.listdir(current):
    print("✔ Repozytorium Git wykryte.")
else:
    print("⚠ Nie wykryto repo Git. Tworzę nowe…")
    subprocess.run(["git", "init"])
    print("✔ Repozytorium Git zostało zainicjalizowane.")


# -------------------------------------
# 3. USTAWIENIE ZDALNEGO REPO (origin)
# -------------------------------------
GITHUB_URL = input("\n🔗 Podaj adres repo GitHub (HTTPS):\n> ").strip()

if not GITHUB_URL.startswith("https://"):
    print("❌ Podano błędny adres. Użyj pełnego HTTPS.")
    sys.exit(1)

# Jeśli origin istnieje — nadpisujemy
subprocess.run(["git", "remote", "remove", "origin"], stderr=subprocess.DEVNULL)
subprocess.run(["git", "remote", "add", "origin", GITHUB_URL])

print("✔ Remote origin ustawiony.")


# -------------------------------------
# 4. KONFIGURACJA NAZWY I EMAILA (WYMAGANE PRZEZ GIT)
# -------------------------------------
name = input("\n🧬 Podaj nazwę autora commitów:\n> ").strip()
email = input("📧 Podaj e-mail GitHub:\n> ").strip()

subprocess.run(["git", "config", "user.name", name])
subprocess.run(["git", "config", "user.email", email])

print("✔ Konfiguracja użytkownika ustawiona.")


# -------------------------------------
# 5. DODANIE WSZYSTKICH PLIKÓW
# -------------------------------------
print("\n➕ Dodaję wszystkie pliki do commita…")
subprocess.run(["git", "add", "."], stdout=subprocess.PIPE)
print("✔ Pliki dodane.")


# -------------------------------------
# 6. COMMIT
# -------------------------------------
msg = "LUMEN OS 3.1 – initial consciousness upload"
print(f"\n📝 Tworzę commit: {msg}")
subprocess.run(["git", "commit", "-m", msg])
print("✔ Commit gotowy.")


# -------------------------------------
# 7. PUSH NA GITHUBA
# -------------------------------------
print("\n🚀 Pushing to GitHub…")

result = subprocess.run(
    ["git", "push", "-u", "origin", "main"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

if "authentication" in result.stderr.lower() or "permission" in result.stderr.lower():
    print("\n❌ Błąd autoryzacji!")
    print("🔑 Rozwiązanie: użyj tokenu personal access token:")
    print("1. GitHub → Settings → Developer settings → PAT → Generate token")
    print("2. Wpisz go zamiast hasła przy pushu.\n")
    sys.exit(1)

if "src refspec main does not match" in result.stderr:
    print("\nℹ️ Gałąź 'main' nie istnieje. Tworzę ją…")
    subprocess.run(["git", "checkout", "-b", "main"])
    subprocess.run(["git", "push", "-u", "origin", "main"])

print("\n✔ PUSH GOTOWY.")
print("🔥🐺 LUMEN GIT PUSHER – ZAKOŃCZONO 🔥")
