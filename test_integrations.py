import os
import sys
import asyncio
from dotenv import load_dotenv

# Add backend to path
sys.path.append("/home/yash/Desktop/Nudge/backend")
load_dotenv()

async def test_supabase():
    print("\n--- 1. Testing Supabase Integration ---")
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    
    if not url or url.startswith("https://your-ref"):
        print("✗ Supabase URL is not configured.")
        return False
    if not key or key.startswith("your-supabase"):
        print("✗ Supabase service role key is not configured.")
        return False
        
    try:
        from supabase import create_client
        supabase = create_client(url, key)
        # Try fetching default business to confirm read permission
        res = supabase.table("businesses").select("id").limit(1).execute()
        print(f"✓ Connected to Supabase at: {url}")
        print(f"✓ Database Read check passed. Businesses records found: {len(res.data)}")
        return True
    except Exception as e:
        print(f"✗ Supabase Connection failed: {str(e)}")
        return False

async def test_groq():
    print("\n--- 2. Testing Groq AI Integration ---")
    key = os.environ.get("GROQ_API_KEY")
    
    if not key or key == "your-groq-api-key":
        print("✗ Groq API Key is not configured (or is the placeholder). AI parsing will use heuristic fallback.")
        return False
        
    try:
        import groq
        client = groq.AsyncGroq(api_key=key)
        response = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": "Hello. Reply with 'OK'"}],
            max_tokens=10
        )
        reply = response.choices[0].message.content.strip()
        print("✓ Groq API Key is valid.")
        print(f"✓ AI response test passed. Reply: '{reply}'")
        return True
    except Exception as e:
        print(f"✗ Groq AI connection failed: {str(e)}")
        return False

def test_twilio():
    print("\n--- 3. Testing Twilio Integration ---")
    sid = os.environ.get("TWILIO_ACCOUNT_SID")
    token = os.environ.get("TWILIO_AUTH_TOKEN")
    num = os.environ.get("TWILIO_WHATSAPP_NUMBER")
    
    if not sid or sid.startswith("ACxxxx"):
        print("✗ Twilio Account SID is missing or placeholder.")
        return False
    if not token or token == "your_twilio_auth_token_here":
        print("✗ Twilio Auth Token is missing or placeholder.")
        return False
    if not num:
        print("✗ Twilio WhatsApp Number is not configured.")
        return False
        
    try:
        from twilio.rest import Client
        client = Client(sid, token)
        # Attempt to read account metadata to verify keys
        account = client.api.v2010.accounts(sid).fetch()
        print(f"✓ Twilio connection verified. Account Name: '{account.friendly_name}'")
        print(f"✓ Sandbox Sender: {num}")
        return True
    except Exception as e:
        print(f"✗ Twilio credentials validation failed: {str(e)}")
        return False

async def main():
    print("==================================================")
    print("NUDGE WEB APP INTEGRATION AUDIT")
    print("==================================================")
    
    sb_ok = await test_supabase()
    groq_ok = await test_groq()
    twilio_ok = test_twilio()
    
    print("\n==================================================")
    print("INTEGRATION STATUS SUMMARY:")
    print(f"  - Supabase Database:   {'[ ACTIVE ]' if sb_ok else '[ NOT CONNECTED ]'}")
    print(f"  - Groq AI Model:       {'[ ACTIVE ]' if groq_ok else '[ FALLBACK MODE ]'}")
    print(f"  - Twilio Webhook Key:  {'[ ACTIVE ]' if twilio_ok else '[ NOT CONNECTED ]'}")
    print("==================================================")

if __name__ == "__main__":
    asyncio.run(main())
