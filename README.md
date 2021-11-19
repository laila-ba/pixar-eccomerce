MAIN IMAGE

[Live Site](https://pixar-ecommerce.herokuapp.com/)

# About

This website is based off of the one and only, Disney Pixar site. Ive always been a fan of Pixar's website as its simple, sleek and minimal while still bringing in their touch of magic and nostalgia from their films. 

# Table of Contents


1. - [User Experience](#UX)
        - [The Strategy Plane](##The-Strategy-Plane)
        - [User Stories](###User-Stories)
    
    ii. [The Scope Plane](## The Scope Plane)
    iii. [The Structure Plane](## The Structure Plane)
    iv. [The Skeleton Plane](## The Skeleton Plane)
        - [Wireframes]()
    v. [The Surface Plane](## The Surface Plane)
        - [Mockups]()
        - [Color Scheme](### Color Scheme)
        - [Typography](### Typography)

2. [Features](# Features)
    - [Features Accross The Site](## Features Accross The Site)
    - [Features Specific To Pages](## Features Specific To Pages)


# UX
## The Strategy Plane

Pixar's film taget audience are very wide as its a universal studio that everyone loves, and therefore doesnt have a niche, specific audience. I wanted to project this through my site so that a large demograpic can easily access the webiste without any difficulty.


### Target Audeince for My Pixar Site :
    - Age: 15-44 as the films are loved by almost everyone including children, teenagers and adults.
    - Users who are big fans of Pixar films.
    - Users who need information on characters or film trailers.
    - Users who are able to use a device connected to the internet
    - Users who want to purchase Pixar toys, clothes and merchandise.
        
### Features:

As part of the planning process for the strategy plane, i find it helpful to plan out which features are of most importance to include in the project on a small scale of 1-3 (3 being the most important.) By doing this technique, i am able to focus more on the higher ranked features and work my way down the table.

FEATURES IMAGE

### User Stories

- #### Shopper Stories
    - I want to view all the products that are available to buy in order to purchase them.
    - I want to be able to view an individual item's details including: price, description, rating, image, available sizes and category
    - I want to be able to see the total of my bag at any time in order to avoid spending much and keep updated.
    - I want to easily be able to sort and filter the available products across all/specific categories, identifying the best rated, best priced and alphabetically sorted.
    - I want to easily acces a specific category of available products.
    - Search for a product by name or description to quickly see if its available.
    - I want to easily select available size and qauntity of product.
    - I want to View items in my bag before purchasing.
    - I want to Adjust or delete quantity of items in my bag.
    - I want to enter payement information easily without hassle and feel safe and secure doing so.
    - I want to view an order confirmation automatically after checkout is successful.
    - I want to recieve an order confirmation email after checking out to keep in records.

- #### Site User Stories
    - I want to be able to easily register for an account and view my profile when logged in.
    - I want ot be able to Easily login and logout
    - Recover my password easily to access my account incase i forget my password.
    - Recieve an email confirmation after registering
    - View my order history, order confirmations and save payement information in my profile.


- #### Store management Stories
    - Add new items to the store easily.
    - Edit and update existing products to change pricing, description images, and other criteria.
    - Delete items that are no longer for sale.

## The Scope Plane
- #### The minimal Product for my project is an e-commerce site with the following features:
    - A payement system
    - A profile page
    - A products page
    - Authorization
- Additional Features can be seen in the [Features]() section.

## The Structure Plane
The structure of my site is outlined below.

- #### Home app 
    #### HTML files
    - The home.html file is the landing page of the whole site. Includes main hero image with a 'discover' link to feature films page. As you scroll down, four links appear to all pages of the site for easy access.

- #### Discover app 
    #### HTML files
    - Includes all html files for each individual film on the feature films template. Each individual film template includes : 
    - Hero image of film.
    - Film logo
    - Film plot 
    - Film trailer
    - Images of characters and their roles within the film
    - The films.html template showcases all feature films that pixar has created. The template includes an Image with the title 'feature films' and all film posters which redirect to individual film templates.

- #### Products app 
    #### HTML files
    - The products.html template is where all available products can be viewed by site users and shoppers. The Products displayed on this page will differ depending on which Category, Brand or specified search query the user is searching by. If none have been selected, it will display all Products available on the site until filtered.
    - The products_detail.html template id shown when a product is clicked on within the products template. The details page shows the product image, description, price, sizes available and quantity. It also gives the user the option to add to bag or keep shopping.
    - The edit_product.html template allows only the admin to edit an existing product.
    - The add _product.html template contains a form for the admin to create and add a new product to the site.
    #### Cateogory Model - Stores Item categories
        name = models.CharField(max_length=254)
    #### Product Model - stores Individual Item information
        category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
        sku = models.CharField(max_length=254, null=True, blank=True)
        name = models.CharField(max_length=254)
        description = models.TextField()
        has_sizes = models.BooleanField(default=False, null=True, blank=True)
        price = models.DecimalField(max_digits=6, decimal_places=2)
        rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
        image_url = models.URLField(max_length=1024, null=True, blank=True)
        image = models.ImageField(null=True, blank=True)

- #### Profiles app 
    #### HTML files
    - The profile.html template displays the user's profile to the user. It contain their saved delivery details and order history. This can only be seen by someone who has registered for an account.
    #### Profile Model - securely stores information on each user. This can be used in checkout to prefill the checkout form.
        user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

- #### Contact app 
    #### HTML files
    - The contact.html template contains a form for site users or shoppers to contact the site admin with any further questions.

- #### Checkout app 
    #### HTML files
    - The checkout.html template displays the final checkout page to the user. It shows them a summary of their order, and gives them a form to complete with their deleivery details. They also input their payement information and once the payement has gone through, they are redirected to the checkout success template.
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

- #### Bag app 
    #### HTML files
    - The bag.html template allows users to view their bag contents, make changes to quantites and delete items from their bag. They also have the option to checkout when they have items in their bag.


## The Skeleton Plane
### Wireframes
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
  <img src="readme-docs/add.png">
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
    
### Mockups
    
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
  <img src="readme-docs/product-details-m.png">
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
  <img src="readme-docs/checkout-success-m.png">
</details>
<details>
  <summary>Bag</summary>
  <img src="readme-docs/bag-m.png">
</details>

## Surface Plane
- ### Color Scheme
  - The color scheme chosen for this project is simple, branching from one primary color: Blue. As the site mainly consists of vibrant images, i thought sticking to various shades of blue would go veyr nicely.
    
    COLOR SCHEME IMAGE

- ### Typography
  - This site uses a variation of two different fonts: Josephin sans & sans-serif.  I chose these two fonts as i took time to compare the fints used on the Pixar site and find something a little similar. I found that when adding letter spacing to these two fonts, it enahnced the simplicity of the site while still appearing similar to the Pixar site.

  TYPO IMAGE

- ### Imagery
  - Imagery is a huge part of the site and is critical to the users as Pixar fans are most appreciative of the clean and shiny graphics. Its used for both informative and entertainmenet purposes as images are displayed in item cards on the products template to allow users to visually engage with items and decide if they are interested to purchase. Images are also shown for aesthetic to bring in the magical and nostalgic feel that Pixar films have.Background images are used a lot throughout the site, the main one being Disney's famous blue sky thats used for their logo and intro to their films. I felt that by encourporating this in images, (as Pixar is one of Disney's brances) and making the colours a part of my site, it enhances the magical, nostalgic theme that my site gives off. I have made sure encorporated atleast one image on every page to keep the feel ongoing throught the site. Product images have been taken from the Disney Site and others have been created and edited through Canva.

  IMAGERY IMAGE

## Features
### Common Features Across All Pages

  - #### Header
    - The header is positioned to be fixed at the top of the screen and to always be visible to the user, no matter what screen size or device is being used. This allows an easy and seamless navigation across all pages, meaning that users can find it quickly.
    - The pixar logo is positioned at the top of the page within the header and when clicked on, redirect you to the home page. The logo is visible in the header when viewed on all screen sizes.
    - The navigation is inside of the header, seen on the right of the header. The pages consist of: Home, films, shop, account and bag. Both shop and account are dropdown menus, revealing more links. The 'shop' link, reveals 'Toys, Adult, Clothing, All Products' and the 'Account' link reveals 'Login, Register' for site visitors, 'Profile' for account holders, and 'Product Management' for the admin profiles. On smaller screens, the navigation collapses into a hamburger menu. This allows the site navigation to be easy and simple to use on all devices.
    - The bag icon is always visible on larger screens, however collapsed into a hamburger menu when on smaller screens. On the Hamburer menu, the bag is centered, standing out from the other links, and easily accessed as the header is fixed.
  - #### Buttons
    - There are two types of buttons throughout the site, both in the same style, just contrasting colours. E.g: one has white text and a blue backgound whereas the other has blue text, blue border and white text. These buttons mostly appear next to eachother when the user is given two options, e.g: 'keep shopping' and 'add to bag'.
  - #### Headings
    - Headings throughout the site appear the same in order for the structure to be easily recognised by the user. The font is always 'Josefin sans' and the letter spacing is constant throughout so that the heading can visibly appear different to the rest of the page and not just be different in size.
  - #### Footer
    - The footer is displayed at the bottom of the page and appears simplistic, corresponding the the colour scheme. It includes a hover effect for every individual social link, when hovered over, an icon appears over the social link and the color changed to the social medias logo colour. Eg: for the Facebook icon, it will turn blue, with an icon above saying 'Facebook'.
  - #### Toasts 
    - The toasts appear to let the user know that they have carried out an action, and whether it was successful. Eg: putting an item in your bag, a message appears showing the user their total of the bag, how much more they need before they get free delivery, and a checkout button. It appears as a pop up message underneath the navigation bar on the right on all devices and can be dismissed by clicking on the 'x' button.

### Features Specific To Pages
  - #### Home Page
    - A large hero image of a well known scene in a Pixar movie. 
    - The heading is a large motivational quote from the movie.
    - Th quote is followed by a 'discover' button that takes the user to the films page to explore their range of feature films.
    - Below the hero image are four cards that are essentially a quick navigation. The cards each have an image on them and a heading to where they redirect to. When each card is hovered over, they scale down and become smaller while covering the card in a house colour background. One of the cards redirects the user to a contact page which isnt shown on the navigation bar. I thought this would be best as i didnt want the nav bar to be overwhelmingly crowded and keep the simplicity flowing through the site. 

  - #### Films Page
    - A large hero image from a Pixar movie with the title of 'FEATURE FILMS'.This lets the user know that these are the main films that Pixar have created.
    - All feature films are diplayed in rows of 3, showing film posters against a white background. The white background works well as each poster includes various vibrant colours and so the white background allows them to stand out more.
    - The films are shown in order, from latest to oldest.
    On the bottom right of the page, a back to top button is shown with a blue arrow to assist the user to scroll up quicker when they have reached near the bottom. This back to top button is visible and available to be clicked on at all times.

  - #### Film details Page