# Imprint Store

![imprint logo](doc/imprint.png)

**Developer: [ Daniel Mullooly - Mulloo ]**

[![Live Site](https://img.shields.io/badge/🌐%20Live%20Site-Visit%20Now-brightgreen?style=for-the-badge)](https://imprint-store-3d6ba50a85bd.herokuapp.com/)
[![GitHub](https://img.shields.io/badge/📁%20GitHub-Repository-blue?style=for-the-badge)](https://github.com/Mulloo/imprint_store)

[![Django](https://img.shields.io/badge/🔥%20Django-3.2.25-green?style=for-the-badge)](https://djangoproject.com/)
[![Python](https://img.shields.io/badge/🐍%20Python-3.x-blue?style=for-the-badge)](https://python.org/)

## Table of Contents

- [About](#about)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
  - [Agile Methodology](#agile-methodology)
  - [Data Model](#data-model)
  - [Testing](#testing)
  - [Security Features and Defensive Design](#security-features-and-defensive-design)
  - [Features](#features)
  - [Validation](#validation)
  - [Technologies Used](#technologies-used)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

---

## About

Imprint Store is a full-stack e-commerce web application built for the Imprint Esports brand. Imprint Esports is a gaming analytics company that provides visual performance indicators for professional esports teams, helping organizations track their players' performance at the highest level of competition.

This online merchandise store serves to promote the Imprint brand while generating revenue through the sale of high-quality branded merchandise including apparel, gaming peripherals, and accessories. The platform delivers a seamless shopping experience with modern web technologies and secure payment processing.

---

## User Experience

### Target Audience

- Esports enthusiasts and fans of competitive gaming
- Supporters of the Imprint Esports brand
- Gamers seeking high-quality branded merchandise
- Users looking for gaming apparel and accessories
- Mobile and desktop users requiring responsive e-commerce functionality

### User Requirements and Expectations

- Intuitive and responsive navigation across all devices
- Comprehensive product browsing with search and filtering capabilities
- Secure user authentication and account management
- Reliable shopping cart and checkout process with multiple payment options
- Order tracking and history functionality
- Professional design reflecting the esports brand identity
- Fast loading times and optimal performance
- Clear product information with high-quality images

---

## User Stories

### Epic 1: User Account Management

- As a **new user**, I can **register for an account** so that **I can access personalized features**
- As a **registered user**, I can **log in and log out** so that **I can securely access my account**
- As a **user**, I can **reset my password** so that **I can regain access to my account**
- As a **user**, I can **update my profile information** so that **my details are current**
- As a **user**, I can **view my order history** so that **I can track my purchases**

### Epic 2: Product Browsing and Search

- As a **shopper**, I can **view all products** so that **I can browse the available merchandise**
- As a **shopper**, I can **search for products** so that **I can find specific items**
- As a **shopper**, I can **filter products by category** so that **I can narrow down my options**
- As a **shopper**, I can **sort products by price, rating, or name** so that **I can organize my browsing**
- As a **shopper**, I can **view detailed product information** so that **I can make informed purchases**

### Epic 3: Shopping Cart and Checkout

- As a **shopper**, I can **add products to my shopping bag** so that **I can purchase multiple items**
- As a **shopper**, I can **modify quantities in my bag** so that **I can adjust my order**
- As a **shopper**, I can **remove items from my bag** so that **I can change my mind about purchases**
- As a **shopper**, I can **securely checkout** so that **I can complete my purchase**
- As a **shopper**, I can **receive order confirmation** so that **I know my purchase was successful**

### Epic 4: Wishlist Management

- As a **registered user**, I can **add products to my wishlist** so that **I can save items for later**
- As a **registered user**, I can **remove products from my wishlist** so that **I can manage my saved items**
- As a **registered user**, I can **view my wishlist** so that **I can see all my saved products**

### Epic 5: Product Reviews

- As a **registered user**, I can **leave reviews for products** so that **I can share my experience**
- As a **registered user**, I can **rate products** so that **I can provide feedback**
- As a **shopper**, I can **read product reviews** so that **I can make informed decisions**

### Epic 6: Site Administration

- As a **store owner**, I can **add new products** so that **I can expand the catalog**
- As a **store owner**, I can **edit product details** so that **I can keep information current**
- As a **store owner**, I can **delete products** so that **I can remove discontinued items**
- As a **store owner**, I can **manage orders** so that **I can process customer purchases**

---

## Design

### Color Scheme

The design follows a professional esports-inspired color palette:

### Color Palette

- **Primary**: #000000 (Black) - Strong, professional
- **Secondary**: #FFFFFF (White) - Clean, modern
- **Accent**: #007BFF (Blue) - Trust, technology
- **Success**: #28A745 (Green) - Positive actions
- **Warning**: #FFC107 (Yellow) - Alerts
- **Danger**: #DC3545 (Red) - Errors

![Imprint Pallet](Docs/imprint_palette.png)

### Typography

- **Primary Font**: Modern, clean sans-serif fonts for optimal readability
- **Headings**: Bold weights for clear hierarchy
- **Body Text**: Regular weights for comfortable reading experience
- **Buttons and CTAs**: Medium weights for clear action items

### Layout and Structure

- **Mobile-First Design**: Responsive layout optimized for mobile devices
- **Grid System**: Bootstrap 4 grid for consistent spacing and alignment
- **Navigation**: Fixed header with collapsible mobile menu
- **Footer**: Organized links and contact information
- **Cards**: Consistent product card design across the site

### Imagery

- **Product Images**: High-quality mockup images for merchandise
- **Brand Logo**: Prominent Imprint Esports branding
- **Icons**: Font Awesome icons for intuitive user interface
- **Background**: Clean, minimal backgrounds to highlight products

---

## Agile Methodology

This project was developed using Agile methodology with the following approach:

### Project Management

- **GitHub Projects**: Used for project planning and tracking
- **Kanban Board**: [View Project Board](https://github.com/users/Mulloo/projects/4)
- **User Stories**: Each feature developed based on user requirements
- **Iterative Development**: Features developed and tested in sprints

### Development Process

1. **Planning**: User stories created and prioritized
2. **Development**: Features built incrementally
3. **Testing**: Continuous testing throughout development
4. **Review**: Regular review and adjustment of priorities
5. **Deployment**: Staged deployment with testing

---

## Data Model

### Entity Relationship Diagram

![Entity Relationship Diagram](Docs/gen-erd.png)

### Core Models

#### User Model (Django Built-in)

- Handles user authentication and basic user information
- Extended by UserProfile model for additional data

#### UserProfile Model

```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
```

#### Product Model

```python
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
```

#### Category Model

```python
class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
```

#### Tag Model (Custom)

```python
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
```

#### Order Model

```python
class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
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
```

#### Wishlist Model (Custom)

```python
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
```

#### ProductReview Model (Custom)

```python
class ProductReview(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    title = models.CharField(max_length=200)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
```

---

## Testing

Comprehensive testing was conducted throughout the development process to ensure functionality, usability, and performance.

### Testing Approach

- **Manual Testing**: Systematic testing of all user journeys
- **User Acceptance Testing**: Real users tested the application
- **Browser Compatibility**: Testing across multiple browsers
- **Responsive Testing**: Verification on various devices
- **Payment Testing**: Stripe test environment validation

### Test Results Summary

- All user authentication flows working correctly
- Product browsing and search functionality verified
- Shopping cart and checkout process tested
- Wishlist management functioning properly
- Review system operational
- Admin functionality working as expected
- Payment processing through Stripe successful
- Email confirmations sending correctly
- Responsive design verified on all device sizes

For detailed testing documentation, see [TEST.md](TEST.MD)

---

## Security Features and Defensive Design

### Authentication Security

- **Django Allauth**: Secure user authentication system
- **Password Hashing**: PBKDF2 password hashing with salt
- **Email Verification**: Account activation via email confirmation
- **Session Management**: Secure session handling with configurable timeouts

### Data Protection

- **CSRF Protection**: Cross-Site Request Forgery protection on all forms
- **SQL Injection Prevention**: Django ORM parameterized queries
- **XSS Prevention**: Template auto-escaping and input sanitization
- **Secure Headers**: HTTP security headers via Django middleware

### Payment Security

- **PCI Compliance**: Stripe handles all sensitive payment data
- **SSL Encryption**: HTTPS enforced for all transactions
- **Webhook Verification**: Stripe webhook signature validation
- **No Card Storage**: Payment information never stored locally

### Environment Security

- **Environment Variables**: Sensitive data stored in environment variables
- **Debug Settings**: Debug mode disabled in production
- **Database Security**: Production database with restricted access
- **AWS S3**: Secure cloud storage for static and media files

---

## Features

### Existing Features

#### User Authentication System

![Login](Docs/login_page.png)
![Sign Up](Docs/register_page.png)

- User registration with email verification
- Secure login/logout functionality
- Password reset capability
- User profile management
- Order history tracking

#### Product Catalog

![Product Catalog](Docs/product_page.png)

- Comprehensive product listings with pagination
- Product search functionality
- Category-based filtering
- Product sorting by price, rating, and name
- Tag-based product discovery

#### Product Detail Pages

![Product Details](Docs/product_details_page.png)

- Detailed product information and images
- Customer reviews and ratings
- Add to cart and wishlist functionality
- Size selection where applicable
- Related product suggestions

#### Shopping Cart System

![Shopping Cart Full](Docs/bag_full.png)
![Shopping Cart Empty](Docs/bag_empty.png)

- Session-based shopping cart
- Quantity adjustment capabilities
- Real-time price calculations
- Delivery cost calculations
- Free delivery threshold notifications

#### Secure Checkout Process

![Checkout Process](Docs/checkout_page.png)

- Stripe payment integration
- Order summary and confirmation
- Delivery information management
- Email confirmation system
- Guest and registered user checkout

#### Wishlist Management

![Wishlist](Docs/wishlist_full_page.png)
![Wishlist](Docs/wishlist_empty.png)

- Personal product wishlist for registered users
- Easy add/remove functionality
- Wishlist persistence across sessions
- Quick access from product pages

#### Review System

![Reviews Profile](Docs/user_review_profile_page.png)
![Reviews Product details Page](Docs/user_review_product_details.png)

- Product review and rating system
- User-generated content moderation
- Review editing and deletion
- Review display with user information

#### Admin Interface

![Admin Interface](Docs/admin_page.png)

- Django admin panel for product management
- Order monitoring and management
- User management capabilities
- Category and tag administration

#### Responsive Design

![Responsive Design](Docs/responsive.png)

- Mobile-first responsive design
- Cross-browser compatibility
- Optimized for all device sizes
- Touch-friendly interface elements

### Features Left to Implement

#### Advanced Functionality

- **Inventory Management**: Stock tracking and low-stock alerts
- **Advanced Product Recommendations**: AI-based suggestion engine
- **Live Chat Support**: Real-time customer service integration
- **Multi-language Support**: Internationalization capabilities

#### Enhanced User Experience

- **Product Comparison**: Side-by-side product comparison tool
- **Advanced Search Filters**: More granular filtering options
- **Social Media Integration**: Enhanced social sharing capabilities
- **Loyalty Program**: Customer rewards and points system

For comprehensive feature documentation, see [FEATURES.md](FEATURES.MD)

---

## Validation

### HTML Validation

- **W3C Markup Validator**: All HTML pages validated
- **Results**: All pages pass validation with no errors

### CSS Validation

- **W3C CSS Validator**: All stylesheets validated
- **Results**: CSS passes validation with no errors

### JavaScript Validation

- **JSHint**: All JavaScript code validated
- **Results**: Code passes validation with no significant issues

### Python Validation

- **PEP8**: All Python code follows PEP8 standards
- **Flake8**: Code linting completed successfully
- **Results**: All Python files conform to style guidelines

### Lighthouse Performance

- **Performance**: 85+ scores across all pages
- **Accessibility**: 90+ scores with WCAG compliance
- **Best Practices**: 90+ scores for security and performance
- **SEO**: 95+ scores for search engine optimization

---

## Technologies Used

### Languages

- **HTML5**: Structure and content markup
- **CSS3**: Styling and layout design
- **JavaScript**: Interactive frontend functionality
- **Python**: Backend development and logic

### Frameworks and Libraries

- **Django 3.2.25**: Web framework for backend development
- **Bootstrap 4**: Frontend framework for responsive design
- **jQuery**: JavaScript library for DOM manipulation
- **Font Awesome**: Icon library for user interface elements

### Databases

- **SQLite**: Development database
- **PostgreSQL**: Production database via Heroku

### Payment Processing

- **Stripe**: Secure payment processing and webhooks

### Cloud Services

- **AWS S3**: Static and media file storage
- **Heroku**: Application hosting and deployment

### Development Tools

- **Git**: Version control system
- **GitHub**: Repository hosting and project management
- **VS Code**: Integrated development environment
- **Chrome DevTools**: Debugging and responsive design testing

### Python Packages

```txt
Django==3.2.25
gunicorn==23.0.0
dj-database-url==0.5.0
psycopg2-binary==2.9.9
django-allauth==0.55.0
django-crispy-forms==1.14.0
django-storages==1.14.4
django-countries==7.6.1
boto3==1.35.31
stripe==10.12.0
Pillow==10.4.0
```

---

## Deployment

### Heroku Deployment

The project was deployed to Heroku using the following steps:

#### Prerequisites

1. **Heroku Account**: Create account at [heroku.com](https://heroku.com)
2. **PostgreSQL Database**: Set up database addon
3. **AWS S3 Bucket**: Configure for static/media files
4. **Stripe Account**: Set up for payment processing

#### Deployment Steps

1. **Create Heroku App**

   ```bash
   heroku create imprint-store-app-name
   ```

2. **Set Config Variables**
   - `DATABASE_URL`: PostgreSQL database URL
   - `SECRET_KEY`: Django secret key
   - `STRIPE_PUBLIC_KEY`: Stripe publishable key
   - `STRIPE_SECRET_KEY`: Stripe secret key
   - `STRIPE_WH_SECRET`: Stripe webhook secret
   - `AWS_ACCESS_KEY_ID`: AWS access key
   - `AWS_SECRET_ACCESS_KEY`: AWS secret key
   - `AWS_STORAGE_BUCKET_NAME`: S3 bucket name
   - `USE_AWS`: Set to True
   - `EMAIL_HOST_USER`: Email service username
   - `EMAIL_HOST_PASS`: Email service password

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Database Migration**

   ```bash
   python manage.py migrate
   ```

5. **Create Superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Collect Static Files**

   ```bash
   python manage.py collectstatic
   ```

7. **Deploy to Heroku**
   - Connect GitHub repository to Heroku
   - Enable automatic deployments
   - Manual deploy from main branch

#### Local Development Setup

1. **Clone Repository**

   ```bash
   git clone https://github.com/Mulloo/imprint_store.git
   cd imprint_store
   ```

2. **Create Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**
   Create `.env` file with required variables

5. **Run Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create Superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run Development Server**

   ```bash
   python manage.py runserver
   ```

#### AWS S3 Configuration

1. **Create S3 Bucket**
   - Set up bucket with public read access
   - Configure CORS policy
   - Set up IAM user with appropriate permissions

2. **Configure Django Settings**

   ```python
   # settings.py
   if 'USE_AWS' in os.environ:
       AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
       AWS_S3_REGION_NAME = 'eu-west-1'
       AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
       AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
   ```

---

## Credits

### Content and Media

- **Imprint Esports Brand**: Used with permission for educational purposes
- **Product Images**: Custom mockup images created for the project
- **Product Descriptions**: Original content written for the project
- **Logo and Branding**: Imprint Esports brand assets (educational use)

### Code References

- **Django Documentation**: Framework implementation guidance
- **Stripe Documentation**: Payment integration tutorials
- **Bootstrap Documentation**: Responsive design patterns
- **Code Institute**: Boutique Ado walkthrough project structure reference
- **Django Allauth Documentation**: Authentication system implementation
- **AWS Documentation**: S3 storage configuration

### Educational Resources

- **Code Institute Full Stack Developer Course**: Primary learning resource
- **Mozilla Developer Network (MDN)**: HTML, CSS, and JavaScript reference
- **Django Girls Tutorial**: Additional Django learning resource
- **Real Python**: Python and Django best practices
- **Stack Overflow**: Problem-solving and debugging assistance

### Tools and Services

- **GitHub**: Repository hosting and version control
- **Heroku**: Application deployment platform
- **AWS S3**: Cloud storage service
- **Stripe**: Payment processing service
- **Font Awesome**: Icon library
- **Google Fonts**: Typography resources

---

## Acknowledgements

I would like to express my gratitude to the following individuals and organizations who contributed to the success of this project:

### Mentorship and Guidance

- **My Code Institute Mentor**: For providing invaluable guidance, feedback, and support throughout the development process
- **Code Institute Tutors**: For technical assistance and problem-solving support
- **Code Institute Community**: For peer support and collaborative learning

### Technical Support

- **Stack Overflow Community**: For providing solutions to technical challenges
- **Django Community**: For comprehensive documentation and community support
- **GitHub Community**: For open-source resources and collaborative development tools

### Testing and Feedback

- **Peer Developers**: For code review and constructive feedback
- **Family and Friends**: For user testing and usability feedback
- **Code Institute Slack Community**: For peer support and testing assistance

### Inspiration and Resources

- **Imprint Esports**: For brand inspiration and concept development (educational use)
- **E-commerce Industry Leaders**: For user experience and design inspiration
- **Open Source Contributors**: For the libraries and frameworks that made this project possible

### Special Thanks

- **Code Institute**: For providing the comprehensive educational program that made this project possible
- **The Django Software Foundation**: For maintaining the excellent Django framework
- **Stripe**: For providing robust payment processing capabilities
- **Heroku**: For reliable application hosting services
- **AWS**: For scalable cloud storage solutions

This project was created as part of the Code Institute Full Stack Software Development Diploma and represents a culmination of the skills and knowledge acquired throughout the program. The support and resources provided by the entire Code Institute ecosystem were instrumental in bringing this project to completion.

---

**[⬆ Back to Top](#table-of-contents)**

---

*This project was developed for educational purposes as part of the Code Institute Full Stack Developer course. The Imprint Esports brand is used with permission for educational purposes only.*
