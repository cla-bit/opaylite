# opaylite Library  ![opaylite](docs/images/opaylite.png)

Opay is a technology company solving payments problems for ambitious businesses. 

This **opaylite API Library** consists of **Opay API** asynchronous and synchronous wrappers, which can be integrated into python projects to interact with **Opay**.

> 📝: Read more on Opay api: https://documentation.opaycheckout.com/


Getting Started
================================================================

You should create a Opay account to generate a **Opay Secret Key, public key and Merchant ID**. You can see this in the Account Details page >> API keys and Webhook section.

> ⚠️: **Warning:** Do not expose your secret key or commit your secret key to git, or use them in client-side code.

> 💡: **Take Note:**  Public key is to be used from your front-end when integrating using Opay Inline. In this case you have to use you secret key

> ✅: **Good**: Set your secret key in environment variables as seen: *Opay_SECRET_KEY=your-secret-key*

# Install opaylite library:
* #### Install opaylite using pip.
> pip install opaylite

or Download the wheel distribution file and install using pip
>  pip install opaylite-0.1.2-py3-none-any.whl 

or Download the source distribution file, change directory and install using pip
> cd 
> 
> pip install opaylite-0.1.2.tar.gz 

or clone from the github repository:
> git clone https://github.com/cla-bit/opaylite.git


[//]: # (# Making a Transaction)

[//]: # ()
[//]: # (If after setting your secret key in environment variables, all you need to do is use the transaction API to make a transaction. )

[//]: # (To make a transaction or initialize a transaction:)

[//]: # ()
[//]: # (* import the Opay API wrapper.)

[//]: # ()
[//]: # (```apacheconf)

[//]: # (    from opaylite import OpayBase)

[//]: # (```)

[//]: # ()
[//]: # (* Create an instance to use the OpayBase wrapper to interact with the Transaction API.)

[//]: # ()
[//]: # (```apacheconf)

[//]: # (    Opay_client = OpayBase&#40;&#41;)

[//]: # (```)

[//]: # ()
[//]: # (* Use the instance and call the transaction method to initialize a transaction)

[//]: # ()
[//]: # (```apacheconf)

[//]: # (    create_transaction = Opay_client.transactions.initialize&#40;)

[//]: # (        email="johndoe@email.com",)

[//]: # (        amount=10000000&#41;)

[//]: # (    )
[//]: # (    print&#40;f"Transaction Created: {create_transaction}"&#41;)

[//]: # (```)

[//]: # ()
[//]: # (> ✅: **Good**: You can check your Opay account, go to the Transaction page and you will see the transaction just created.)

[//]: # ()
[//]: # ()
[//]: # (# Other Tools)

[//]: # (Similar to calling the OpayBase, you can also call other tools to make your work easy. For example:)

[//]: # ()
[//]: # (* ### Account Type)

[//]: # (```apacheconf)

[//]: # (    from opaylite import AccountType)

[//]: # (    )
[//]: # (    val1 = AccountType.PERSONAL.value)

[//]: # (    )
[//]: # (    print&#40;val1&#41;)

[//]: # (```)

[//]: # (> "personal")

[//]: # ()
[//]: # (* ### Convert units to subunits:)

[//]: # (```apacheconf)

[//]: # (    from opaylite import convert_to_subunit)

[//]: # (    )
[//]: # (    # amount should be in subunit in this case 10000 kobo = 100 naira)

[//]: # (    money = convert_to_subunit&#40;100, Currency.NGN&#41;)

[//]: # (    print&#40;money&#41;)

[//]: # (```)

[//]: # (> 10000)

[//]: # ()
[//]: # (* ### Channels)

[//]: # (```apacheconf)

[//]: # (    from opaylite import Channels)

[//]: # (    )
[//]: # (    bank = Channels.BANK.value)

[//]: # (    )
[//]: # (    print&#40;bank&#41;)

[//]: # (```)

[//]: # (> "bank")

[//]: # ()
[//]: # (* ### Currency)

[//]: # (```apacheconf)

[//]: # (    from opaylite import Currency)

[//]: # (    )
[//]: # (    val1 = Currency.NGN.value)

[//]: # (    )
[//]: # (    print&#40;val1&#41;)

[//]: # (```)

[//]: # (> "NGN")

[//]: # ()
[//]: # (* ### Document Type)

[//]: # (```apacheconf)

[//]: # (    from opaylite import DocumentType)

[//]: # (    )
[//]: # (    val1 = DocumentType.IDENTITY_NUMBER.value)

[//]: # (    )
[//]: # (    print&#40;val1&#41;)

[//]: # (```)

[//]: # (> "identityNumber")

[//]: # ()
[//]: # (Others are: ***EventType, Interval, MobileMoney, PWT, QRCODE, RecipientType, ResendOTP, Resolution, RiskAction, SplitType, STATUS, and USSD***.)
