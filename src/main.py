from keyword_listener import wait_for_keyword

if wait_for_keyword("jarvis"):
    print("✅ Keyword detected!")
else:
    print("❌ Keyword not detected.")
