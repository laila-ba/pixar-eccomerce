<img src="readme-docs/README-hero.png">


# About

This website is based on the one and only, Disney Pixar site. I've always been a fan of Pixar's website as it's simple, sleek, and minimal while still bringing in their touch of magic and nostalgia from their films. The [Live Site](https://pixar-ecommerce.herokuapp.com/) can be viewed here.

* ### NOTE: MOST IMAGES AND TEXT HAVE BEEN TAKEN FROM DISNEY PIXAR*


# The Strategy Plane

Pixar's film target audience is very wide as it is a universal studio that everyone loves, and therefore doesn't have a niche, specific audience. I wanted to project this through my site so that a large demographic can easily access the website without any difficulty.


## Target Audience for My Pixar Site :
    - Age: 15-44 as the films are loved by almost everyone including children, teenagers, and adults.
    - Users who are big fans of Pixar films.
    - Users who need information on characters or film trailers.
    - Users who can use a device connected to the internet
    - Users who want to purchase Pixar toys, clothes, and merchandise.
        
## Features:

As part of the planning process for the strategy plane, I find it helpful to plan out which features are of most importance to include in the project on a small scale of 1-3 (3 being the most important.) By doing this technique, I can focus more on the higher-ranked features and work my way down the table.

<img src="readme-docs/features.png">

## User Stories

- ### Shopper Stories
    - I want to view all the products that are available to buy.
    - I want to be able to view an individual item's details including price, description, rating, image, available sizes, and category
    - I want to be able to see the total of my bag at any time to avoid spending much and keep updated.
    - I want to easily be able to sort and filter the available products across all/specific categories, identifying the best rated, best priced, and alphabetically sorted.
    - I want to easily access a specific category of available products.
    - Search for a product by name or description to quickly see if it is available.
    - I want to easily select the available size and quantity of product.
    - I want to View items in my bag before purchasing.
    - I want to Adjust or delete the number of items in my bag.
    - I want to enter payment information easily without hassle and feel safe and secure doing so.
    - I want to view an order confirmation automatically after checkout is successful.
    - I want to receive an order confirmation email after checking out to keep in records.

- ### Site User Stories
    - I want to be able to easily register for an account and view my profile when logged in.
    - I want to be able to Easily login and logout
    - Recover my password easily to access my account in case I forget my password.
    - View my order history, order confirmations, and save payment information in my profile.


- ### Store management Stories
    - Add new items to the store easily.
    - Edit and update existing products to change pricing, description images, and other criteria.
    - Delete items that are no longer for sale.

## The Scope Plane
- ### The minimal end Product for my project is an e-commerce site with the following features:
    - A payment system
    - A profile page
    - A products page
    - Authorization

## The Structure Plane
The structure of my site is outlined below.

- ### Home app 
    #### HTML files
    - The home.html file is the landing page of the whole site. Includes main hero image with a 'discover' link to feature films page. As you scroll down, four links appear to all pages of the site for easy access.

- ### Discover app 
    #### HTML files
    - Includes all HTML files for each film on the feature films template. Each film template includes : 
    - Hero image of the film.
    - Film logo
    - Film plot 
    - Film trailer
    - Images of characters and their roles within the film
    - The films.html template showcases all feature films that Pixar has created. The template includes an Image with the title 'feature films' and all film posters which redirect to individual film templates.

- ### Products app 
    #### HTML files
    - The products.html template is where all available products can be viewed by site users and shoppers. The Products displayed on this page will differ depending on which Category, Brand or specified search query the user is searching by. If none have been selected, it will display all Products available on the site until filtered.
    - The products_detail.html template id shown when a product is clicked on within the products template. The details page shows the product image, description, price, sizes available and quantity. It also gives the user the option to add to bag or keep shopping.
    - The edit_product.html template allows only the admin to edit an existing product.
    - The add _product.html template contains a form for the admin to create and add a new product to the site.
    ### Cateogory Model - Stores Item categories
        name = models.CharField(max_length=254)
    ### Product Model - stores Individual Item information
        category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
        sku = models.CharField(max_length=254, null=True, blank=True)
        name = models.CharField(max_length=254)
        description = models.TextField()
        has_sizes = models.BooleanField(default=False, null=True, blank=True)
        price = models.DecimalField(max_digits=6, decimal_places=2)
        rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
        image_url = models.URLField(max_length=1024, null=True, blank=True)
        image = models.ImageField(null=True, blank=True)

- ### Profiles app 
    #### HTML files
    - The profile.html template displays the user's profile to the user. It contains their saved delivery details and order history. This can only be seen by someone who has registered for an account.
    #### Profile Model - securely stores information on each user. This can be used in checkout to prefill the checkout form.
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        default_phone_number = models.CharField(max_length=20, null=True, blank=True)
        default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
        default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
        default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
        default_county = models.CharField(max_length=80, null=True, blank=True)
        default_postcode = models.CharField(max_length=20, null=True, blank=True)
        default_country = CountryField(blank_label='Country', null=True, blank=True)

- ### Contact app 
    #### HTML files
    - The contact.html template contains a form for site users or shoppers to contact the site admin with any further questions.

- ### Checkout app 
    #### HTML files
    - The checkout.html template displays the final checkout page to the user. It shows them a summary of their order and gives them a form to complete with their delivery details. They also input their payment information and once the payment has gone through, they are redirected to the checkout success template.
    - The checkout_success.html template gives the shopper an order confirmation with a summary with all of the details of the order and the personal details the user put in on the page prior.
    #### Order Model - Holds information of each order, and is created when a user completes the checkout.
        order_number = models.CharField(max_length=32, null=False, editable=False)
        user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
        full_name = models.CharField(max_length=50, null=False, blank=False)
        email = models.EmailField(max_length=254, null=False, blank=False)
        phone_number = models.CharField(max_length=20, null=False, blank=False)
        country = CountryField(blank_label='Country *', null=False, blank=False)
        postcode = models.CharField(max_length=20, null=True, blank=True)
        town_or_city = models.CharField(max_length=40, null=False, blank=False)
        street_address1 = models.CharField(max_length=80, null=False, blank=False)
        street_address2 = models.CharField(max_length=80, null=True, blank=True)
        county = models.CharField(max_length=80, null=True, blank=True)
        date = models.DateTimeField(auto_now_add=True)
        delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
        order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
        grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
        original_bag = models.TextField(null=False, blank=False, default='')
        stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    #### OrderLine Model - is used for calucations in the Order Model
        order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
        product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
        product_size = models.CharField(max_length=2, null=True, blank=True) # XS, S, M, L, XL
        quantity = models.IntegerField(null=False, blank=False, default=0)
        lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

- ### Bag app 
    #### HTML files
    - The bag.html template allows users to view their bag contents, make changes to quantities and delete items from their bag. They also have the checkout option when they have items in their bag.


# The Skeleton Plane
## Wireframes
<details>
  <summary>Home</summary>
  <img src="readme-docs/home.png">
</details>
<details>
  <summary>Films </summary>
  <img src="readme-docs/films.png">
</details>
<details>
  <summary>Films details </summary>
  <img src="readme-docs/film-detail.png">
</details>
<details>
  <summary>Shop </summary>
  <img src="readme-docs/shop.png">
</details>
<details>
  <summary>Login </summary>
  <img src="readme-docs/login.png">
</details>
<details>
  <summary>Register </summary>
  <img src="readme-docs/register.png">
</details>
<details>
  <summary>Profile </summary>
  <img src="readme-docs/profile.png">
</details>
<details>
  <summary>Product Details </summary>
  <img src="readme-docs/product_detail.png">
</details>
<details>
  <summary>Add product(Admin) </summary>
  <img src="readme-docs/Add.png">
</details>
<details>
  <summary>Checkout </summary>
  <img src="readme-docs/checkout.png">
</details>
<details>
  <summary>Checkout Success</summary>
  <img src="readme-docs/checkout_success.png">
</details>
<details>
  <summary>Bag</summary>
  <img src="readme-docs/bag.png">
</details>

 ---   

## Mockups
    
<details>
  <summary>Home</summary>
  <img src="readme-docs/Home-m.png">
</details>
<details>
  <summary>Films</summary>
  <img src="readme-docs/feature films-m.png">
</details>
<details>
  <summary>Film Details</summary>
  <img src="readme-docs/Film details-m.png">
</details>
<details>
  <summary>Shop</summary>
  <img src="readme-docs/shop-m.png">
</details>
<details>
  <summary>Login</summary>
  <img src="readme-docs/login-m.png">
</details>
<details>
  <summary>Register</summary>
  <img src="readme-docs/register-m.png">
</details>
<details>
  <summary>Profile</summary>
  <img src="readme-docs/profile-m.png">
</details>
<details>
  <summary>Product Details</summary>
  <img src="readme-docs/product details-m.png">
</details>
<details>
  <summary>Add Product(Admin)</summary>
  <img src="readme-docs/admin.png">
</details>
<details>
  <summary>Checkout</summary>
  <img src="readme-docs/checkout-m.png">
</details>
<details>
  <summary>Checkout Success</summary>
  <img src="readme-docs/checkout success-m.png">
</details>
<details>
  <summary>Bag</summary>
  <img src="readme-docs/bag-m.png">
</details>

# Surface Plane
- ## Color Scheme
  - The color scheme chosen for this project is simple, branching from one primary color: Blue. As the site mainly consists of vibrant images, I thought sticking to various shades of blue would go very nicely.
    
    <img src="readme-docs/color2.png">

- ## Typography
  - This site uses a variation of two different fonts: Josephin sans & sans-serif.  I chose these two fonts as I took the time to compare the fonts used on the Pixar site and find something a little similar. I found that when adding letter spacing to these two fonts, it enhances the simplicity of the site while still appearing similar to the Pixar site.

    <img src="readme-docs/typo.png">

- ## Imagery
  - Imagery is a huge part of the site and is critical to the users as Pixar fans are most appreciative of the clean and shiny graphics. It is used for both informative and entertainment purposes as images are displayed in item cards on the products template to allow users to visually engage with items and decide if they are interested to purchase. Images are also shown for aesthetics to bring in the magical and nostalgic feel that Pixar films have. Background images are used a lot throughout the site, the main one being Disney's famous blue sky that's used for their logo and intro to their films. I felt that by incorporating this in images, (as Pixar is one of Disney's branches) and making the colors a part of my site, it enhances the magical, nostalgic theme that my site gives off. I have made sure to incorporate at least one image on every page to keep the feel ongoing throughout the site. Product images have been taken from the Disney Site and others have been created and edited through Canva.

    <img src="readme-docs/imagery.png">

# Features
## Common Features Across All Pages

  - ### Header
    - The header is positioned to be fixed at the top of the screen and to always be visible to the user, no matter what screen size or device is being used. This allows easy and seamless navigation across all pages, meaning that users can find it quickly.
    - The Pixar logo is positioned at the top of the page within the header and when clicked on, redirects you to the home page. The logo is visible in the header when viewed on all screen sizes.
    - The navigation is inside of the header, seen on the right of the header. The pages consist of Home, films, shop, account, and bag. Both shop and account are dropdown menus, revealing more links. The 'shop' link, reveals 'Toys, Adult, Clothing, All Products' and the 'Account' link reveals 'Login, Register' for site visitors, 'Profile' for account holders, and 'Product Management' for the admin profiles. On smaller screens, the navigation collapses into a hamburger menu. This allows the site navigation to be easy and simple to use on all devices.
    - The bag icon is always visible on larger screens, however collapsed into a hamburger menu when on smaller screens. On the Hamburger menu, the bag is centered, standing out from the other links, and easily accessed as the header is fixed.
  - ### Buttons
    - There are two types of buttons throughout the site, both in the same style, just contrasting colors. E.g: one has white text and a blue background whereas the other has blue text, blue border, and white text. These buttons mostly appear next to each other when the user is given two options, e.g: 'keep shopping' and 'add to bag'.
  - ### Headings
    - Headings throughout the site appear the same for the structure to be easily recognized by the user. The font is always 'Josefin sans' and the letter spacing is constant throughout so that the heading can visibly appear different from the rest of the page and not just be different in size.
  - ### Footer
    - The footer is displayed at the bottom of the page and appears simplistic, corresponding to the color scheme. It includes a hover effect for every individual social link, when hovered over, an icon appears over the social link and the color changed to the social media logo color. Eg: for the Facebook icon, it will turn blue, with an icon above saying 'Facebook'.
  - ### Toasts 
    - The toasts appear to let the user know that they have carried out action and whether it was successful. Eg: putting an item in your bag, a message appears showing the user their total of the bag, how much more they need before they get free delivery, and a checkout button. It appears as a pop-up message underneath the navigation bar on the right on all devices and can be dismissed by clicking on the 'x' button.

## Features Specific To Pages
  - ### Home Page
    - A large hero image of a well-known scene in a Pixar movie. 
    - The heading is a large motivational quote from the movie.
    - Th quote is followed by a 'discover' button that takes the user to the films page to explore their range of feature films.
    - Below the hero image are four cards that are essentially quick navigation. The cards each have an image on them and a heading to where they redirect. When each card is hovered over, they scale down and become smaller while covering the card in a house color background. One of the cards redirects the user to a contact page that isn't shown on the navigation bar. I thought this would be best as I didn't want the navbar to be overwhelmingly crowded and keep the simplicity flowing through the site. 

  - ### Films Page
    - A large hero image from a Pixar movie with the title of 'FEATURE FILMS'.This lets the user know that these are the main films that Pixar has created.
    - All feature films are displayed in rows of 3, showing film posters against a white background. The white background works well as each poster includes various vibrant colors and so the white background allows them to stand out more.
    - The films are shown in order, from latest to oldest.
    - On the bottom right of the page, a back-to-top button is shown with a blue arrow to assist the user to scroll up quicker when they have reached near the bottom. This back-to-top button is visible and available to be clicked on at all times.

  - ### Film details Page
    - A large hero image from the chosen film and the film's logo is below.
    - A summary of the film's plot to perhaps remind the user what the film is about.
    - The film's trailer can be played on the page without the user leaving to go to Youtube. The trailer can be played and paused at any time and can also be viewed on full screen. This is responsive on all devices.
    - A heading of the character names, followed by their images and a summary. This is done for each character.
    - A back-to-top button for the user to navigate around easily.

  - ### Shop Page
    - A large hero image with the title of 'SHOP' followed by a smaller sub-heading.
    - A search bar enables shoppers to search for a specific item quickly.
    - Items displayed in a responsive grid layout to be responsive on all screen sizes.
    - The image of items is above important information such as the items title, price, category, and rating.
    - Item image can be clicked to bring the user to the details page.
    - Filter button is available and can be toggled to collapse or reveal sorting options.
  
  - ### Products Detail Page
    - Shows both product and description info on a responsive grid layout to accommodate all screen sizes.
    - Product image is large, and when clicked on, the image opens up in a separate tab.
    - Product title, price, category, rating, and description are available.
    - Shoppers can choose the quantity they want to put in their bag for that product.
    - A 'keep shopping' button is available for users to navigate back to the shop page quickly. 
    - A 'add to bag' button allows users to add products to their bag efficiently.

  - ### Login & Register page
    - Both these pages have the same layout to have a clear design structure.
    - login and register forms are displayed on a card with an image alongside the form. 
    - Register form enables users to register with an email which they must confirm after, and a password that fits within the requirements.
    - Register page has two buttons at the bottom: 'back to login' which takes them to the login page in case they already have an account and a sign-up button which then asks them to verify their email.
    - The login page has two buttons at the bottom: 'home' which offers the user easy navigation for them to be redirected to the home page and 'sign in' which takes the user to the home page and gives them a message notification to let them know that they are signed in.

  - ### Bag page
    - When the bag is empty, an image appears with a Pixar character crying and some text saying that their bag is empty. Below this, there is a 'shop' button enabling the user to be redirected to the products page to fill up their bag.
    - When the bag has products inside, the product info appears alongside the quantity chosen, subtotal, and delivery cost. 
    - Two buttons are placed under the quantity button: 'update' and 'remove'. These allow the user to edit any items in their basket; they can increase or decrease the amount they already have, and they can delete items.
    - There are two buttons at the bottom of the page: 'Keep shopping' and 'secure checkout' which offer easy navigation for the user to the products page or the checkout page.

  - ### Delivery/Checkout Page
    - The shopper's order summary is displayed on the right and the user's details will be displayed on the left as a form layout. This allows the user to edit and add their details to the delivery. On smaller screen sizes, the order summary is shown first, and below is the details form.
    - Delivery Details are provided as a form using crispy forms.
    - Users are given the option to save their delivery details to their profile if they have one,  otherwise, they are offered sign-in and sign-up buttons.
    - Users are provided with a secure checkout using stripe to enter their bank details.

  - ### Checkout Success Page
    - A thank you image is displayed at the top of the page.
    - The user is presented with their order information alongside a confirmation email being sent to them.
    - A button at the bottom of the information: 'keep shopping'.

  - ### Profile Page
    - A form is displayed with the user's default delivery information and can be edited and updated for checkout. 
    - The shopper's order history is displayed on the right, showing their order number, date, items, and order total.
    - The users can click on a past order's confirmation number and it will take them to the checkout success page. However, they have displayed a message at the top of the screen alerting them that it is a past order.

  - ### Product management page (admin)
    - The *' add a product'* page allows the admin to fill out a form to add a product to appear on the products page and for shoppers to be able to purchase it. The admin can create a description, rating, price title, category, sizes, image URL or upload an image from their local device.
    - The *' edit a product'* page allows the admin to edit a product in any aspect. The category, SKU, name, description, sizes, price, rating, and image can all be edited and changed from the shop page.
    - Products can be deleted by the admin from the products page. Besides every product, is two button links: 'edit' and 'delete'

  - ### Contact
    - A form displayed on the page where the users can fill in the information asked and send their message to the site Admin

  ### Future Features to Add
    - Add different types of delivery options to choose from other than a default delivery.
    - Add an apple pay option to payments
    - Admin can receive messages sent from site users from the contact page into the desired email.

# Testing
## Functionality

  - ### Navigation bar
    - The navigation bar is fixed at the top of any device and stays visible when the site is being scrolled.
    - All navigation links take the user to the relevant pages.
    - The shop link is a dropdown menu, when clicked on, it reveals a menu with item categories that bring the user to the products page with the selected category displayed and items filtered.
    - The logo is a clickable link,  taking the user to the home page when clicked on.
    - The My Account link is a dropdown, revealing 'login' and 'register' for new users, allowing existing users to access their account, and new members to join. When a user is successfully logged in, the dropdown menu reveals 'logout' 'profile'. 
    - The cart icon takes the user to the bag page to view what items are already inside, or if it is empty. Below the cart, they can see how much the total items are that the user has chosen. When items are in the bag, the icon turns blue, standing out from the other links.
    - When each link in the user dropdown is clicked, the user is navigated to the appropriate page.
    - The navbar is fully responsive. On smaller device viewports, the navbar collapses and a hamburger menu button is displayed instead.
    - When the hamburger button is clicked, the main menu items are revealed and all work fine. The bag icon is placed at the bottom of the menu in the middle to stand out.
    - When the menu is opened, scrolling is still enabled on the page, however, the menu stays fixed and on top of all content. 
    - When the hamburger menu is clicked again, the navigation bar closes.

  - ### The Footer
    - Footer is accessible and visible on all pages except the checkout page when the user clicks on the checkout button to purchase any items. This is done so that nothing can interfere with any purchases that the users are making and to avoid any errors.
    - When social links are clicked in the footer, they are redirected to the relevant page.
    - When hovered over, the icons have a filled-in background and the name of the social media appears above to help the user identify which link will be clicked on.
    - Footer always stays at the bottom of the page, below any content.

  - ### Registration
    - The user can register and become a member by clicking on the register button from the main nav bar dropdown as they are directed to the registration form page.
    - Users can click on the sign-up buttons in various alluth pages such as the Login page.
    - Within the sign-up form, all fields are required to be filled out, otherwise, the allauth displays a validation message. 
    - Allauth will send validation errors if valid emails are not given, passwords are too short, do not match or are too common/easy, emails do not match.
    - When 'Sign Up' is clicked with a valid form, the user is redirected to a page with a message displayed to let the user know that an email has been sent and they have to validate their e-mail address. This page includes a button to redirect the user to the contact page if they have not received an email.
    - User receives an e-mail from Pixar with a link that brings the user to the 'Confirm E-mail Address'. When 'confirm" is clicked on this page, the user is re-directed to the 'Sign In' page alongside a pop-up message saying 'email verified'
    - When a new user registers successfully, their profile is created automatically.

  - ### Log Out / Log in
    - A validation error will appear if username/e-mail and/or password were incorrect. It doesn't specify which field is incorrect so that malicious users don't know specifically which field was incorrect.
    - Users can log in using their existing Pixar Account.
    - The login validation form will display a validation message if either password or username/e-mail are left empty.
    - If the user clicks on 'Forgot Password', they are navigated to a page where they are asked to enter their e-mail address. They will then receive an e-mail with a link to reset the password and also remind them what their username is. When the link is clicked, the user is asked to enter the new password twice. If this is successful, the user is navigated to a success page with a button to redirect the user back to the login.
    - When the user is resetting their password, a validation error will appear if the passwords do not match.
    - The sign-up link on the login page function as expected.
    - When the user clicks on 'logout', they are redirected to a page asking them if they would like to log out or not. If yes, the user's session is removed, they are logged out and redirected to the home page as a non-authenticated user.
    - When a user logs in, they are redirected to the home page and shown a message that they are logged in.

- ### Home page
  - Home page is responsive on all devices.
  - All links are working a take the user to the relevant pages. 
  - The discover button takes the user to the films page to discover Pixar's feature films.
  - Navigation cards at the bottom of the page all have smooth animation and work as expected.

- ### Shop Page
  - When the shop link dropdown is clicked on, it reveals a menu with item categories that bring the user to the products page with the selected category displayed and items filtered.
  - The search bar is visible on the Shop page to allow users to search for the items that they are looking for.
  - The search bar is fully responsive and is scaled to fit on any device.
  - When the input is focused on, the border of the search bar has a blue box-shadow to show the user they can now type inside of it. 
  - When an empty form is submitted, a pop-up message appears underneath the navigation bar letting the user know that they didn't enter a search criteria
  - If a search criterion is entered and no results are found, the user is told so by a message below the search bar.
  - When the user enters in search criteria and presses search, the page refreshes and auto scrolls down to the section of found products.
  - There is a sort button below the search bar which reveals sorting buttons that sort selected items by added date, price, or alphabetical order. If the filter button is clicked again, the sorting buttons disappear.
  - All products within the page are laid out in a grid design, making it responsive on any device. Items appear in rows of 4 on large screens, 3 n medium, 2 on small, and 1 item per row is shown on normal mobile view.
  - Each product has a visible image, rating, title, price, and category.
  - When an Item's image is clicked, the user is redirected to the item's page where they can add to their bag.

- ### Product Details Page
  - The product detail page displays the product image on the left side and the product title, price, category, rating, and description on the other side. 
  - The Page also includes the available sizes for the user to choose from and a quantity toggle button that increases and decreases when the user clicks -/+. 
  - The user can only choose a max of 10 in the quantity of an item otherwise they will get an error.
  - The layout is responsive on all devices and the image and details move all to one column when viewed on mobile view.
  - Below the page, there is an 'add to bag' button that allows the user to add the item to their bag. A bag notification then appears, letting the user know that the item has been added.
  - The 'keep shopping' button redirects the user back to the products page.
  - When the main image of a product is clicked on, a separate tab is opened with the individual image alone.

- ### Film Page
  - Films are shown in a layout grid of 3 posters per row. This is responsive across all devices as images decrease in size when viewed on smaller devices.
  - The back to top button is always displayed at the bottom right of the page, and when clicked on, takes the user to the top of the page making navigation easier and smoother.
  - When film posters are clicked on, the user is redirected to the relevant film details page.

- ### Film Details Pages
  - The film details pages include a relevant summary of each film.
  - A trailer video of the specific film. When the user clicks on the play button, The film's trailer can be played on the page without the user leaving to go to Youtube. The trailer can be played and paused at any time and can also be viewed on full screen. This is responsive on all devices.
  - The trailer can also be watched on youtube if the user clicks on the youtube logo on the video as a new tab opens up with the relevant video.
  - Each film details page includes images of all relevant characters and a summary of them.
  - The back to top button is always displayed at the bottom right of the page, and when clicked on, takes the user to the top of the page making navigation easier and smoother.

- ### Bag page & toasts
  - When a user adds an item to their bag, it is added to the bag and a notification appears letting the user know it is in their bag. The bag icon total also updates on the navigation bar.
  - Within the notification toast, the user can see the item/items image, price, quantity, and total that they have added.
  - When the user updates the item's quantity or deletes an item from the bag, a toast appears showing the current bag total and a message letting the user know that they have done so successfully.
  - From bag toast, if the user clicks on 'Secure checkout', they are navigated to the Shopping bag page.
  - From the bag toast, when 'Secure Checkout' is clicked, the user is navigated to the checkout page.
  - If the last item was removed from the bag, the page refreshes, the bag is displayed as empty and the toast appears, telling the user that they have removed the item.
  - If a bag is empty, an image appears alongside a 'hey you!' title telling the user that their bag is empty. There is a button below saying 'Shop' which will redirect the user to the shop page where they can add items to their bag.
  - Users can be redirected to the bag page from the navbar, bag toast, or checkout page.
  - If the user has items in their bag, they can view a summary of their items alongside the image, title, the size chosen, SKU, quantity subtotal, delivery fee, and a message informing the user how much more they need to spend to get free delivery.
  - When the 'remove' button is clicked, the item is removed from the bag.
  - When the quantity toggle +/- button is clicked on, the quantity changes and when the user clicks on the 'update' button, the quantity is updated. This refreshes the page and also updates the subtotal and if there is any, the delivery fee.

- ### Checkout & checkout success Page
  - The checkout page displays the order summary, Delivery, Shipping, and Payment Info form.
  - Within the details form, all fields are required to be filled in except from the 'street address 2' 'county' and 'post code'. 
  - When required fields are not filled out, validation will prompt the user to fill them in.
  - If the user enters invalid card details, Stripe will return an error message for the user to try again.
  - When the form has been filled out correctly, and the user clicks on 'complete order', they are displayed with a loading spinner where they are not able to click on anything within the page until the payment has succeeded. The user is then are re-directed to the Checkout Success page where they can see their order details and confirmation email has been sent.
  - If the user is not logged in, they can log in or sign up using the links under the Delivery Form to save their delivery information.
  - If the user is logged in already, they are given an option to save their shipping details to their profile with a checkbox.

- ### Profile Page
  - The profile page is only accessible to authenticated users who have made accounts. It can be accessed through the 'my account' dropdown menu in the navigation bar.
  - Users can fill out the form to save their delivery information to become the default when checking out.
  - The user can edit the default information in the form and save them in the database by clicking 'update information'.
  - Users can view their order history from their profile account underneath the title 'order history'.
  - Within the order history, users can view their order number, the date and time of the purchase, the items and their quantity, and the order total.
  - Orders in the order history are shown in order from oldest to latest.
  - The users can click on a past order's confirmation number and it will take them to the checkout success page. However, they are displayed a message at the top of the screen alerting them that it is a past order.

- ### Contact Page
  - The contact page can be found on the bottom of the home page and when the user clicks on the image with the text 'contact', they are redirected to the contact page.
  - The user can fill in their full name, email address, and message within a form.
  - There are two buttons at the bottom of the page: 'cancel' and 'send'.
  - The user can only click send once all fields are filled in within the form.
  - Once the send button is clicked alongside a valid form, the user sees a pop-up message confirming that their message has been sent and they are then redirected back to the home page.
  - If the user clicks on the 'cancel' button, they are redirected to the home page, and no further action is taken.

# Validators
## HTML5
<details>
  <summary>Home - Pass</summary>
  <img src="readme-docs/home-html-check.png">
</details>
<details>
  <summary>Films - Pass</summary>
  <img src="readme-docs/films-html-check.png">
</details>
<details>
  <summary>Film Details - Pass</summary>
  <img src="readme-docs/film-detail-html-check.png">
</details>
<details>
  <summary>Shop - Pass</summary>
  <img src="readme-docs/shop-html-check.png">
</details>
<details>
  <summary>Product Details - Pass (1 warning advising for me to remove type attribute from script tag.)</summary>
  <img src="readme-docs/product-detail-html-check.png">
</details>
<details>
  <summary>Log In - Pass</summary>
  <img src="readme-docs/login-html-check.png">
</details>
<details>
  <summary>Register - Pass</summary>
  <img src="readme-docs/signup-html-check.png">
</details>
<details>
  <summary>Bag - Pass</summary>
  <img src="readme-docs/bag-html-check.png">
</details>
<details>
  <summary>Checkout Success- Pass</summary>
  <img src="readme-docs/success-html-check.png">
</details>
<details>
  <summary>Checkout- Pass (2 warnings advising for me to remove type attribute from script tag.)</summary>
  <img src="readme-docs/checkout-html-check.png">
</details>
<details>
  <summary>Contact- Pass </summary>
  <img src="readme-docs/contact-html-checker.png">
</details>

## CSS

- #### Checkout.css- Pass

- #### Contact.css- Pass

- #### Profile.css- Pass

- <details>
  <summary>Base.css- Pass (NOTE: When validating base.css, the validator returned 1 error associated with not recognizing variables in linear gradient. If variables were overwritten by regular color names, the validator passes.)</summary>
  <img src="readme-docs/color.png">
</details>

## JSHINT

- #### Countryfield.js - Pass

- #### Home/script.js - Pass

- #### Contact.js - Pass

- #### Stripe_Elements.js - Pass

# Compatibilty
- Browser Compatibility:

  <img src="readme-docs/table.png">

- The devices that were used during testing were: iPad pro, iPhone 12, iPhone 12 mini, windows desktops with 27" screens, Dell Laptop, and various Andriod devices.
- Responsively was used to view my site from various devices simultaneously, helping me spot errors. The different devices varied from  Galaxy Fold (280px) to large Desktop ViewPorts.

# Performance Testing - User Stories
- ### Shopper Stories

  1. I want to view all the products that are available to buy to purchase.
      - All available products can be viewed on the Shop page and can be filtered. The shop page is accessible from the navigation bar and the Shop image at the bottom of the Home page.

  2. I want to be able to view an individual item's details including price, description, rating, image, available sizes, and category
      - Users can view product details easily by clicking on the product's image and they are instantly redirected to the product details page. The page displays the product image on the left side and the product title, price, category, rating, sizes, and description on the other side.

  3. I want to be able to see the total of my bag at any time to avoid spending much and keep updated.
      - The total of the shopper's bag is always visible on the navigation bar, underneath the bag icon. On mobile view, this is still visible, however, the shopper must open the hamburger menu to view the bags total.
      - When a user adds an item to their bag, it is added to the bag and a notification appears letting the user know it is in their bag.

  4. I want to easily be able to sort and filter the available products across all/specific categories, identifying the best rated, best priced, and alphabetically sorted.
      - On the shop page, where all available products are listed, there is a sort button below the search bar which reveals sorting buttons that sort selected items by added date, price, or alphabetical order. If the filter button is clicked again, the sorting buttons disappear.

  5. I want to easily access a specific category of available products.
      - Users can easily access specific categories through the navigation bar, within the Shop dropdown. All categories are listed there, including an option for all categories to be displayed.

  6. Search for a product by name or description to quickly see if it is available.
      - Within the shop page, the search bar is visible to allow users to search for the items that they are looking for.
      - When the user enters in search criteria and presses search, the page refreshes and auto scrolls down to the section of found products.
  
  7. I want to easily select the available size and quantity of product.
      - Within the product details page, includes the available sizes for the user to choose from and a quantity toggle button that increases and decreases when the user clicks -/+.
      - Users can also choose their desired sizes here.

  8. I want to View items in my bag before purchasing.
      - The user can view a summary of their chosen items on the bag page before the checkout. 
  
  9. I want to Adjust or delete the number of items in my bag.
      - Users can easily adjust and delete items from their bags. When the quantity toggle +/- button is clicked on, the quantity changes, and when the user clicks on the 'update' button, the quantity is updated.
      - Users can also remove items from their basket when the 'remove' button is clicked.

  10. I want to enter payment information easily without hassle and feel safe and secure doing so.
      - Payments are handled by Stripe, securely, they are encrypted and card details are not shared with anyone.

  11. I want to view an order confirmation automatically after checkout is successful.
      - Shoppers are redirected to the checkout success page once their payment has gone through successfully. They can then see their order details and a confirmation email has been sent.

  12. I want to receive an order confirmation email after checking out to keep in the record.
      - Order history is sent automatically after payment has been successful. An order confirmation is displayed on the screen as well.
  
  - ### Site User Stories
    1. I want to be able to easily register for an account and view my profile when logged in.
        - The user can register and become a member by clicking on the register button from the main nav bar dropdown as they are directed to the registration form page.
        - Register page only needs the user's e-mail, username, and password.
        - E-mail verification arrives almost instantly so the user doesn't have to wait a long time.
        - Once the users have verified their email, they can log in straight away and view their profile.

    2. I want to be able to Easily log in and log out.
        - Users can navigate to log in and log out easily through the navigation bar.

    3. Recover my password easily to access my account in case I forget my password.
        - Users can recover their password by clicking on the 'forgot password link. They are then asked to enter their email address and an email is sent instantly for them to recover their password.

    4. View my order history, order confirmations, and save payment information in my profile.
        - Logged-in user can access their Order history page from their profile.
        - The users can click on a past order's confirmation number and it will take them to the checkout success page. However, they are displayed a message at the top of the screen alerting them that it is a past order.
  
   - ### Store management Stories
    1. Add new items to the store easily.
        - The admin can add new items through the  'add a product' page that allows the admin to fill out a form to add a product to appear on the products page and for shoppers to be able to purchase it. The admin can create a description, rating, price title, category, sizes, image URL or upload an image from their local device.

    2. Edit and update existing products to change pricing, description images, and other criteria.
        - The admin can edit items through the 'edit a product' page that allows the admin to edit a product in any aspect. The category, SKU, name, description, sizes, price, rating, and image can all be edited and changed from the shop page.

    3. Delete items that are no longer for sale.
        - The admin can delete products that are no longer available through the shop page by clicking on the 'delete' button below every product on the page.

# Bugs
## Identified Bugs
  1. ### My toast messages were not appearing when adding items to the bag. 
  <img src="readme-docs/toast-before.png">

  - My messages were not being triggered for items with no sizes, meaning when items of clothing were added to the basket, no toasts were appearing.
  - I added the following code for sized items to also trigger toasts: 

            if size:
            if item_id in list(bag.keys()):
                if size in bag[item_id]['items_by_size'].keys():
                    bag[item_id]['items_by_size'][size] += quantity
                    messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
                else:
                    bag[item_id]['items_by_size'][size] = quantity
                    messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
            else:
                bag[item_id] = {'items_by_size': {size: quantity}}
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            if item_id in list(bag.keys()):
                bag[item_id] += quantity
                messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
            else:
                bag[item_id] = quantity
                messages.success(request, f'Added {product.name} to your bag')

            
  2. ### When I checkout a bag with items, the success message appears in the console and the payment goes through to stripe, but I get an error saying " 'AnonymousUser'   object is not iterable"

        - I realized that within my view, I was not checking whether the user is authenticated when saving profile data. I added the following if statement to the code that fixed the bug: 

        if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

  3. ### When trying to push to Heroku, I got the following error: 

        main -> main (shallow update not allowed)
        error: failed to push some refs to 'https://git.heroku.com/pixar-ecommerce.git'

  - I then noticed that the Procfile wasn't matching the WSGI_APPLICATION value in settings.py:

    <img src="readme-docs/proc.png">

  - After changing up the typo to the correct matching spelling, the error was fixed.

  4. ### My webhook handlers were failing with a 404 error and failed stripe webhooks
      - I took a close look into the webhooks.py file and after some time, realized that the return statement in webhooks.py is causing the problem. With that return on line 37, the webhook handler never gets to process the webhook. There only needs to be a return response at the bottom of the file. Once removing this, the bug was fixed.

       <img src="readme-docs/webhook.png">

# Existing Bugs

  - The quantity toggle button on the products details page can be changed by changing the HTML in the dev tools. E.g: the maximum amount a shopper can choose is 10, however, this can be overwritten through the dev tools. This will be fixed in future versions.

  - Website not loading on Iam responsive. I received an x-frame error and the site would not load.

# Technologies used

* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/What_is_CSS)
* [JavaScript](https://www.javascript.com/)
* [Python](https://www.python.org/)
* [Pip3](https://pip.pypa.io/en/stable/)- install packages to python
* [Git](https://git-scm.com/)- version control
* [GitHub](https://github.com/)- host project files
* [Gitpod](https://www.gitpod.io/)- coding enviroment
* [Django](https://www.djangoproject.com/)- main framework for project
* [Heroku](https://id.heroku.com/login)- cloud platform
* [Django Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/)- displays forms
* [Stripe](https://stripe.com/gb) - used as secure payement system
* [AWS](https://aws.amazon.com/) - Used to store static files
* [Bootstrap 5](https://getbootstrap.com/) - Used for responsiveness
* [Font Awsome](https://fontawesome.com/) - Used for icons such as footer
* [Figma](https://www.figma.com/) - Used for mockups ad wireframes
* [Canva](https://www.canva.com/en_gb/) - Used for created custom images

# Deployment

1. Within the project repository, You can either:
    - Download the files by clicking on 'Code' and then 'Download Zip'

      <img src="readme-docs/zip.png">

    ### OR..

    - Clone the repository by running the following command from your IDE

          gh repo clone laila-ba/Pixar-eccomerce
    
2. After doing this, within your chosen IDE, make sure you are inside the project folder by using 

           cd The/Project/Folder/Path

3. Activate virtual enviroment:
    - Python's venv source 
            .venv/bin/activate
    
    - Using Windows and macOS, .venv is the name you gave previously

4. Install all requirements from requirements.txt file

          pip3 install -r requirements.txt
  - After this, create a file named 'env.py' to store all environment variables like so:

            os.environ.setdefault('SECRET_KEY', '<your-variable-goes-here>')
            os.environ.setdefault('DEVELOPMENT', '1')
            os.environ.setdefault('ALLOWED_HOSTS', '<your-variable-goes-here>')
            os.environ.setdefault('STRIPE_PUBLIC_KEY', '<your-variable-goes-here>')
            os.environ.setdefault('STRIPE_SECRET_KEY', '<your-variable-goes-here>')
            os.environ.setdefault('STRIPE_WH_SECRET_CH', '<your-variable-goes-here>')
            os.environ.setdefault('STRIPE_WH_SECRET_SUB', '<your-variable-goes-here>')
  - Lastly run the app with:

             python3 manage.py runserver

# Credits
- [neumorphism-generator](https://hype4.academy/tools/neumorphism-generator) for cards used in the project
- Product Images and product descriptions taken from [Disney](https://www.shopdisney.co.uk/)