# Meta Developer App ও Access Token Setup Guide

## ধাপ ১: Meta for Developers এ রেজিস্ট্রেশন ও লগইন
- [Meta for Developers](https://developers.facebook.com/) ওয়েবসাইটে গিয়ে Facebook একাউন্ট দিয়ে লগইন করো।
- নিশ্চিত করো তোমার Developer Account সঠিকভাবে তৈরি হয়েছে।

## ধাপ ২: নতুন অ্যাপ তৈরি করা
- ড্যাশবোর্ড থেকে **Create App** বাটনে ক্লিক করো।
- App Type হিসেবে **Business** অথবা **None** বেছে নাও (তোমার প্রজেক্টের প্রয়োজন অনুযায়ী)।
- অ্যাপের নাম দাও, যেমন: `SQA Auto Poster`।
- তোমার ইমেইল ঠিকানা প্রবেশ করিয়ে **Create App** ক্লিক করো।

## ধাপ ৩: Facebook Login পণ্য যুক্ত করা (Optional)
- সাধারণত পোস্ট করার জন্য এই ধাপ প্রয়োজন হয় না, তাই এই ধাপ এড়িয়ে যেতে পারো।

## ধাপ ৪: Facebook Page Access Token তৈরি করা

### ৪.১: Facebook Graph API Explorer ব্যবহার করে Token নেয়া
- [Graph API Explorer](https://developers.facebook.com/tools/explorer) এ যাও।
- বাম উপরের কোণে তোমার তৈরি করা অ্যাপ সিলেক্ট করো।
- **Access Token** সেকশনে গিয়ে **Get Token** > **Get User Access Token** ক্লিক করো।
- নিচের পারমিশনগুলো সিলেক্ট করো:
  - `pages_show_list`
  - `pages_manage_posts`
  - `pages_read_engagement`
  - `pages_manage_engagement`
- **Generate Access Token** করে Token নাও।

### ৪.২: Page Access Token পেতে API কল করো
- User Access Token পেলে নিচের API কল করো:

```bash
https://graph.facebook.com/v17.0/me/accounts?access_token=USER_ACCESS_TOKEN
```

API রেসপন্স থেকে তোমার Facebook Page এর Access Token (access_token ফিল্ড) খুঁজে বের করো।

## ধাপ ৫: Token ও Page ID তোমার .env ফাইলে সংরক্ষণ
.env ফাইলে নিচের তথ্যগুলো যোগ করো:
```
FB_PAGE_ID=your_facebook_page_id
FB_ACCESS_TOKEN=your_page_access_token
```
Access Token এর মেয়াদ সীমিত হতে পারে, তাই প্রয়োজনে Token রিফ্রেশ করতে হতে পারে।

Then Run `python app.py` file
