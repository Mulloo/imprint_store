# TESTING - Imprint Store

## Manual Testing

Testing was done throughout site development, for each feature before it was merged into the master file.

Usability was tested with the below user acceptance testing, sent to new users to ensure testing from different users, on different devices and browsers to ensure issues were caught and where possible fixed during development.

| Page    | User Actions           | Expected Results | Y/N | Comments    |
|-------------|------------------------|------------------|------|-------------|
| **Authentication** |                        |                  |      |             |
| Sign Up     | Click on Sign Up button | Redirection to Sign Up page | Y |          |
| 1           | Enter valid email | Field accepts email format | Y |          |
| 2           | Enter valid password | Field accepts password format | Y |          |
| 3           | Click Sign Up button | User account created, email confirmation sent | Y |          |
| 4           | Click confirmation link in email | Account activated, redirect to login | Y |          |
| **Login**   |                        |                  |      |             |
| 1           | Enter valid credentials | User logged in successfully | Y |          |
| 2           | Enter invalid credentials | Error message displayed | Y |          |
| 3           | Click "Remember Me" | User stays logged in | Y |          |
| **Navigation** |                        |                  |      |             |
| 1           | Click on logo | Redirect to home page | Y |          |
| 2           | Click "All Products" | Redirect to products page | Y |          |
| 3           | Click category links | Filter products by category | Y |          |
| 4           | Click shopping bag icon | Redirect to bag page | Y |          |
| 5           | Click profile icon | Dropdown menu appears | Y |          |
| 6           | Click wishlist icon | Redirect to wishlist page | Y |          |
| **Product Browsing** |                        |                  |      |             |
| 1           | View products page | All products displayed | Y |          |
| 2           | Use search bar | Relevant products shown | Y |          |
| 3           | Filter by category | Products filtered correctly | Y |          |
| 4           | Sort products (price, name, etc.) | Products sorted correctly | Y |          |
| 5           | Click product image | Redirect to product details | Y |          |
| **Product Details** |                        |                  |      |             |
| 1           | View product details | All product info displayed | Y |          |
| 2           | Select quantity | Quantity selector works | Y |          |
| 3           | Click "Add to Bag" | Product added to bag | Y |          |
| 4           | Click "Add to Wishlist" | Product added to wishlist | Y |          |
| 5           | View product images | Image gallery functions | Y |          |
| **Shopping Bag** |                        |                  |      |             |
| 1           | View bag contents | All bag items displayed | Y |          |
| 2           | Update quantities | Quantities updated, totals recalculated | Y |          |
| 3           | Remove items | Items removed from bag | Y |          |
| 4           | View bag total | Correct total displayed | Y |          |
| 5           | Click "Secure Checkout" | Redirect to checkout | Y |          |
| **Checkout Process** |                        |                  |      |             |
| 1           | Fill delivery details | Form accepts valid data | Y |          |
| 2           | Save delivery info (logged in) | Info saved to profile | Y |          |
| 3           | Enter payment details | Stripe form validates | Y |          |
| 4           | Complete order | Order processed successfully | Y |          |
| 5           | View order confirmation | Confirmation page displayed | Y |          |
| 6           | Receive confirmation email | Email sent to customer | Y |          |
| **User Profile** |                        |                  |      |             |
| 1           | View profile page | Profile info displayed | Y |          |
| 2           | Update default info | Changes saved successfully | Y |          |
| 3           | View order history | Past orders displayed | Y |          |
| 4           | Click order number | Order details displayed | Y |          |
| **Wishlist** |                        |                  |      |             |
| 1           | View wishlist | All wishlist items shown | Y |          |
| 2           | Add product to wishlist | Product added successfully | Y |          |
| 3           | Remove from wishlist | Product removed successfully | Y |          |
| 4           | Add wishlist item to bag | Product added to bag | Y |          |
| **Admin Panel** |                        |                  |      |             |
| 1           | Access admin login | Admin login page displayed | Y |          |
| 2           | Add new product | Product added successfully | Y |          |
| 3           | Edit existing product | Changes saved successfully | Y |          |
| 4           | Delete product | Product deleted successfully | Y |          |
| 5           | Manage categories | Categories managed successfully | Y |          |
| 6           | View orders | All orders displayed | Y |          |

## Browser Compatibility Tests

| Browser | Status | Notes |
|---------|--------|-------|
| Chrome | PASS | All features working |
| Firefox | PASS | All features working |
| Safari | PASS | All features working |
| Edge | PASS | All features working |

## Mobile Responsiveness Tests

| Device Type | Status | Notes |
|-------------|--------|-------|
| Mobile Phone | PASS | Navigation collapses correctly |
| Tablet | PASS | Layout adapts appropriately |
| Desktop | PASS | Full functionality available |

## Performance Tests

| Test | Status | Notes |
|------|--------|-------|
| Page load times | PASS | Average < 3 seconds |
| Image loading | PASS | Images optimized |
| Stripe payment processing | PASS | Processing under 5 seconds |

## User Story Testing

### First Time Visitor Goals

| User Story | Requirement Met | Evidence |
|------------|----------------|----------|
| As a first-time visitor, I want to understand the purpose of the site | Y | Clear branding and product categories |
| As a first-time visitor, I want to browse products easily | Y | Intuitive navigation and search |
| As a first-time visitor, I want to create an account | Y | Registration process works |

### Returning Visitor Goals

| User Story | Requirement Met | Evidence |
|------------|----------------|----------|
| As a returning visitor, I want to log in quickly | Y | Login form accessible |
| As a returning visitor, I want to view my order history | Y | Profile page shows past orders |
| As a returning visitor, I want to manage my wishlist | Y | Wishlist functionality works |

### Frequent User Goals

| User Story | Requirement Met | Evidence |
|------------|----------------|----------|
| As a frequent user, I want to checkout quickly | Y | Saved delivery info speeds process |
| As a frequent user, I want to track my orders | Y | Order status visible in profile |
| As a frequent user, I want personalized experience | Y | Wishlist and saved preferences |

### Admin Goals

| User Story | Requirement Met | Evidence |
|------------|----------------|----------|
| As an admin, I want to manage products | Y | Admin panel provides full CRUD |
| As an admin, I want to view orders | Y | Order management available |
| As an admin, I want to manage users | Y | User management through admin |

## Payment Testing

| Test Scenario | Card Number | Expected Result | Status |
|---------------|-------------|-----------------|--------|
| Successful payment | 4242424242424242 | Payment succeeds | PASS |
| Declined payment | 4000000000000002 | Payment declined | PASS |
| Authentication required | 4000002500003155 | 3D Secure authentication | PASS |
| Insufficient funds | 4000000000009995 | Payment fails | PASS |

## Security Testing

| Test | Status | Notes |
|------|--------|-------|
| CSRF protection | PASS | All forms protected |
| SQL injection prevention | PASS | ORM prevents injection |
| XSS prevention | PASS | Template escaping active |
| Secure payment processing | PASS | Stripe handles sensitive data |

## Accessibility Testing

| Test | Status | Notes |
|------|--------|-------|
| Keyboard navigation | PASS | All elements accessible |
| Screen reader compatibility | PASS | Alt text on images |
| Color contrast | PASS | WCAG AA compliant |
| Form labels | PASS | All inputs labeled |

## Known Issues

- Minor: Toast messages may overlap on very small screens
- Minor: Product images may load slowly on slower connections

## Test Environment

- **Browsers**: Brave, LiberWolf, Arc, Floor, Mullvad Browser.
- **Devices**: Windows PC, Linux Laptop, Fire Max 11, Galaxy S24 Ultra.
- **Operating Systems**: Windows, Fire OS, Linux
