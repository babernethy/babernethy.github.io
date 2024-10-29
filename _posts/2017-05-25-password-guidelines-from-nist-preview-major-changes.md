---
title: 'Password guidelines from NIST preview major changes'
date: '2017-05-25T09:09:30+00:00'
image: /assets/images/nist_logo_thumb.png
tag: security
---

![Image](/assets/images/nist_logo_thumb.png "NIST LOGO")

## Passwords still don’t work. 

Even after years of thinking up ways of making them harder to guess but still easy enough to remember, people still have passwords that are easily guessed and abused. A draft guideline from the National Institute of Standards and Technology (NIST) is looking to change things yet again, and it really does look like some good changes. Today’s password standards usually look something like this: Use a password that is 10+ characters, make sure you use a capital letter somewhere, a lower-case letter somewhere, a number, and maybe something that isn’t a letter or a number – oh and change it every 3 months or so just in case. So how many people used something like My1GoodP@ssword!, then My2GoodP@ssword!, etc. (and then promptly forgot which letter was the @ and what number you were on).

The new standards from NIST ([DRAFT NIST Special Publication 800-63B – Digital Identity Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html)) make more sense. NIST uses the terminology “

1. Let/require them to be longer – a **longer password** is the only way to beat “brute force” attacks (i.e. checking all possible combinations of passwords – the most logical ones first). NIST is upping the maximum length recommendation to 64 characters)
2. “**Do not impose other composition rules** (e.g. mixtures of different character types) on memorized secrets.” – that is, don’t make you use a number or “other character” – people tend to forget these and thus require a reset of the password more often.
3. “**Do not require that memorized secrets be changed arbitrarily** (e.g., periodically)” – if you come up with a really good password, you should be able to keep it for a while …
4. When people change their passwords, **quality check the password** and give the user feedback. So on the back-end you should use a routine that will check the password against a list of the most common passwords (“black list”) and a common rule set for the most commonly used passwords. If the password is a common one, or too easy to guess, then require the user to enter a different/better password.

So then you can use something like “***LiveLongAndProsper***” – which is a very familiar quote to Star Trek fans, so on the surface looks pretty weak, but actually scores very well on a password strength test (such as [The Password Meter](http://www.passwordmeter.com/)).

This is still a DRAFT of the new standards, but if finalized it should be something you’ll see sites move to in the near future – this will take some time. But I think the overall impact on sites that use passwords will be a positive one … I probably should write a follow up on using a Password Manager and PIV key for even more password security …