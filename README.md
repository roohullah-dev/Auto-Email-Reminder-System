# 📧 Auto Email Reminder System using Python

A smart automation system that reads invoice data from Google Sheets and sends **personalized email reminders** to clients—automatically, beautifully, and on time.

## ✨ What This Project Does

This Python script helps freelancers, businesses, and developers automate client reminders using a simple Google Sheet. It ensures no unpaid invoice goes unnoticed by sending styled HTML emails, optionally with attached PDF invoices.

## 🔥 Features

- 🔗 **Live Google Sheet integration** — reads your invoice records in real-time via CSV
- 📧 **Smart reminder logic** — sends reminders only to unpaid clients on or after their reminder date
- 🎨 **Elegant HTML email template** — modern, responsive, and polite message formatting
- 📎 **PDF invoice attachment support** — includes invoice as a PDF if available
- 🔐 **Secure using `.env`** — your credentials are safe with environment variables
- 🕒 **Automated scheduling** — run daily using Windows Task Scheduler or CRON

## 🗂️ Project Structure

```
auto_email/
├── main.py                  # Main script for execution
├── custom_auto_email.py     # Email sending logic (SMTP, HTML formatting, attachment)
├── .env                     # Email credentials (securely loaded)
├── invoices/                # Store your invoice PDFs here
└── README.md                # This file
```

## 🧾 Google Sheet Format (CSV Export)

Make sure your Google Sheet contains these columns:

| email              | name       | invoice_no | amount | due_date   | reminder_date | has_paid |
| ------------------ | ---------- | ---------- | ------ | ---------- | ------------- | -------- |
| client@example.com | John Smith | INV-123    | 120    | 2025-07-20 | 2025-07-15    | no       |

🔗 _Publish your Google Sheet using:_  
**File → Share → Publish to Web → CSV Format**

## 📤 Sample Email Output

> **Subject:** `Python Automation Expert Invoice INV-123`

```
Hi John,  
I hope you are well.  
This is a kind reminder that $120 for invoice INV-123 is due on 20-07-2025.  
Please confirm if everything is on track for payment.  
Best regards,  
Roohullah

```

📎 _If available, a PDF version of the invoice will be attached automatically._

## 🔐 Environment Setup

Create a `.env` file:

```
EMAIL=roohanitech121@gmail.com
PASSWORD=your_email_app_password
```

⚠️ Use an **App Password** if using Gmail with 2FA enabled.

## 🧠 How It Works

1. Loads the latest data from your Google Sheet
2. Filters rows:
   - Where `has_paid == no`
   - Where `reminder_date <= today`
3. Sends a custom email with optional PDF attachment
4. Prints log of emails sent

## 🔄 Scheduling (Automation)

You can automate daily runs via:

- ✅ **Windows Task Scheduler** (ideal for Windows)
- ✅ **CRON jobs** (Linux/macOS)

## 💡 Use Cases

- Freelancers reminding clients about payment
- SaaS startups automating invoicing
- Small businesses reducing manual email follow-up

## 📞 Contact

If you need a **customized email automation tool**, tailored to your use case (e.g., weekly reports, marketing campaigns, order summaries), feel free to reach out:

- 💼 **Fiverr:** https://www.fiverr.com/roohullah2020/
- 📧 **Email:** roohullahdev5@gmail.com

## ❤️ Final Note

This project is more than code—it's a tool to **save your time**, **streamline your communication**, and help you **get paid faster**.

I built this with care so you don't have to chase invoices manually anymore. Let automation work while you focus on what matters most.

> Made with 💻 and 💙 by **Roohullah**
