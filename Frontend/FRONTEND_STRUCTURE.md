# Frontend Directory Structure Documentation

This document provides a complete overview of the frontend folder structure for the Boarding Finder application.

## Project Root: Frontend/

```
Frontend/
├── BACKEND_STRUCTURE.md     # Backend documentation reference
├── FRONTEND_STRUCTURE.md    # This file - Frontend documentation
├── media/                   # User-uploaded files and media storage
├── static/                  # Static assets (CSS, JavaScript, images)
│   ├── css/                 # Stylesheets
│   │   └── style.css        # Main application stylesheet
│   ├── js/                  # JavaScript files
│   │   └── (empty - ready for JS modules)
│   └── images/              # Static images
│       └── (empty - ready for image assets)
└── templates/               # Django HTML templates
    ├── layouts/             # Base template layouts
    │   └── base.html        # Master template with navbar and footer
    ├── includes/            # Reusable template components
    │   ├── navbar.html      # Navigation bar component
    │   └── footer.html      # Footer component
    ├── home/                # Homepage and landing page templates
    │   ├── home.html        # Main homepage
    │   ├── hero.html        # Hero section component
    │   ├── search.html      # Search bar component
    │   ├── featured.html    # Featured listings component
    │   ├── how_it_works.html # Process explanation component
    │   ├── locations.html   # Location showcase component
    │   ├── cta.html         # Call-to-action component
    │   ├── testimonials.html # User testimonials component
    │   └── why_choose.html  # Value proposition component
    ├── accounts/            # User authentication and profile pages
    │   ├── login.html       # User login page
    │   ├── register.html    # User registration page
    │   ├── profile.html     # User profile page
    │   └── forgot_password.html # Password reset page
    ├── boarding/            # Boarding listings and details
    │   ├── list.html        # Boarding listings page
    │   ├── card.html        # Boarding listing card component
    │   ├── details.html     # Boarding detailed information page
    │   ├── gallery.html     # Boarding image gallery component
    │   ├── amenities.html   # Amenities display component
    │   ├── filters.html     # Search/filter options component
    │   ├── information.html # Boarding information component
    │   ├── owner_info.html  # Boarding owner/landlord info component
    │   ├── pagination.html  # Pagination component
    │   ├── booking_form.html # Booking form component
    │   └── reviews.html     # Reviews and ratings component
    └── dashboard/           # User dashboard pages
        └── (empty - ready for dashboard templates)
```

## Directory Descriptions

### Root Level

| Item | Purpose |
|------|---------|
| `media/` | Storage for user-uploaded content (profile photos, room images, documents) |
| `static/` | Static web assets that don't change (CSS, JavaScript, icons) |
| `templates/` | Django Jinja2 templates for rendering HTML pages |

---

## Static Assets Directory: `static/`

### CSS Directory (`static/css/`)

| File | Purpose |
|------|---------|
| `style.css` | Main stylesheet containing all application styles, colors, typography, and responsive design rules |

**Future Structure:**
```
css/
├── style.css        # Main stylesheet
├── responsive.css   # Mobile and responsive styles
├── components.css   # Reusable component styles
├── forms.css        # Form styling
└── animations.css   # Animations and transitions
```

### JavaScript Directory (`static/js/`)

Currently empty - ready for JavaScript modules.

**Recommended Future Structure:**
```
js/
├── main.js          # Entry point
├── utils.js         # Utility functions
├── filters.js       # Filter functionality
├── booking.js       # Booking form handling
├── search.js        # Search functionality
└── modal.js         # Modal/dialog handling
```

### Images Directory (`static/images/`)

Currently empty - ready for static image assets.

**Expected Content:**
- Logo files
- Icon sets
- Background images
- Default placeholder images

---

## Templates Directory: `templates/`

### Layout Templates: `layouts/`

#### `base.html`
- **Purpose:** Master template for all pages
- **Contains:** Basic HTML structure, header, footer, and template blocks
- **Extends:** None (parent template)
- **Used by:** All other templates inherit from this
- **Key Blocks:**
  - `{% block content %}` - Main page content
  - `{% block extra_css %}` - Additional stylesheets
  - `{% block extra_js %}` - Additional scripts

---

### Reusable Components: `includes/`

#### `navbar.html`
- **Purpose:** Navigation bar component
- **Location:** Included in base.html header
- **Contains:** Logo, main navigation links, user menu, authentication links
- **Links Include:**
  - Home
  - Browse Boardings
  - Dashboard (if logged in)
  - Login/Register (if not logged in)
  - User Profile (if logged in)

#### `footer.html`
- **Purpose:** Footer component
- **Location:** Included in base.html footer
- **Contains:** Company info, quick links, social media, contact info, copyright

---

### Homepage Templates: `home/`

#### `home.html`
- **Purpose:** Main landing page
- **Includes:** hero.html, search.html, featured.html, how_it_works.html, locations.html, testimonials.html, cta.html, why_choose.html
- **Layout:** Full-page composition with multiple sections

#### `hero.html`
- **Purpose:** Hero section at top of homepage
- **Contains:** Main headline, tagline, background image/video, primary call-to-action button

#### `search.html`
- **Purpose:** Search functionality bar
- **Contains:** Location input, date range picker, amenities filter, search button
- **Functionality:** Quick search access from homepage

#### `featured.html`
- **Purpose:** Display featured/promoted boarding listings
- **Contains:** Grid/carousel of featured properties
- **Shows:** High-quality listings, ratings, price information

#### `how_it_works.html`
- **Purpose:** Step-by-step process explanation
- **Contains:** 
  - Step 1: Browse listings
  - Step 2: View details
  - Step 3: Make booking
  - Step 4: Confirm reservation

#### `locations.html`
- **Purpose:** Popular locations showcase
- **Contains:** List or map of popular boarding locations, area highlights

#### `testimonials.html`
- **Purpose:** User reviews and success stories
- **Contains:** Testimonial cards with user quotes, ratings, user photos

#### `cta.html`
- **Purpose:** Call-to-action section
- **Contains:** Engaging message to encourage signup/booking
- **Typical Layout:** Banner with headline and button

#### `why_choose.html`
- **Purpose:** Value proposition section
- **Contains:** Features and benefits of the platform
- **Highlights:**
  - Verified listings
  - Secure transactions
  - 24/7 support
  - Easy booking process

---

### Account Management Templates: `accounts/`

#### `login.html`
- **Purpose:** User login page
- **Contains:** Email/username input, password input, login button, forgot password link, sign up link
- **Extends:** base.html
- **Form:** Django login form

#### `register.html`
- **Purpose:** New user registration page
- **Contains:** 
  - First name input
  - Last name input
  - Email input
  - Password input
  - Password confirmation
  - Terms acceptance checkbox
  - Register button
  - Login link for existing users
- **Extends:** base.html
- **Form:** Django registration form

#### `profile.html`
- **Purpose:** User profile and account settings
- **Contains:**
  - Profile picture upload
  - Personal information (name, email, phone)
  - Address and location
  - Bio/about me
  - Account settings
  - Change password option
  - Account preferences
- **Extends:** base.html
- **Access:** Requires authentication

#### `forgot_password.html`
- **Purpose:** Password reset request page
- **Contains:** Email input, submit button, back to login link
- **Flow:** User enters email → receives reset link
- **Extends:** base.html

---

### Boarding Listings Templates: `boarding/`

#### `list.html`
- **Purpose:** Display all boarding listings
- **Contains:** filters.html, pagination.html, grid/list of boarding cards
- **Functionality:** 
  - Display multiple boarding listings
  - Sidebar or header filters
  - Pagination controls
- **Extends:** base.html

#### `card.html`
- **Purpose:** Individual boarding listing card component
- **Contains:**
  - Property image (gallery thumbnail)
  - Property name/title
  - Location/address
  - Price per month
  - Star rating
  - Number of reviews
  - Quick amenities summary
  - Favorite/bookmark button
- **Used In:** list.html, featured.html
- **Reusable:** Yes - used in multiple places

#### `details.html`
- **Purpose:** Comprehensive boarding information page
- **Contains:** 
  - gallery.html
  - information.html
  - amenities.html
  - owner_info.html
  - booking_form.html
  - reviews.html
- **Extends:** base.html
- **Full Information:** Complete property details

#### `gallery.html`
- **Purpose:** Image gallery/slideshow component
- **Contains:** Multiple property images with navigation
- **Features:**
  - Image carousel/lightbox
  - Thumbnail navigation
  - Full-screen view option
  - Image count indicator

#### `information.html`
- **Purpose:** Property details and description
- **Contains:**
  - Property description
  - Room count
  - Bed count
  - Bathroom count
  - Size/area
  - Rent price details
  - Lease terms
  - Available since date
  - Property type
  - Contact information

#### `amenities.html`
- **Purpose:** Display available amenities/facilities
- **Contains:** Icons and descriptions of amenities
- **Examples:**
  - WiFi
  - Parking
  - Laundry
  - Kitchen
  - Air Conditioning
  - Water Supply
  - Security
  - Common Areas

#### `owner_info.html`
- **Purpose:** Information about property owner/landlord
- **Contains:**
  - Owner profile picture
  - Owner name
  - Verified badge (if applicable)
  - Member since date
  - Response rate
  - Contact button
  - Message button
  - Owner reviews/ratings

#### `booking_form.html`
- **Purpose:** Booking reservation form
- **Contains:**
  - Check-in date picker
  - Check-out date picker (optional)
  - Duration selection
  - Number of occupants
  - Special requests text area
  - Terms acceptance
  - Submit booking button
- **Functionality:** Calculate total price based on dates

#### `reviews.html`
- **Purpose:** Display user reviews and ratings
- **Contains:**
  - Star rating display (overall)
  - Review count
  - Individual review cards with:
    - Reviewer name
    - Rating
    - Review text
    - Review date
    - Reviewer photo (optional)
  - Add review button (if authenticated)
  - Review pagination

#### `filters.html`
- **Purpose:** Search and filter options
- **Contains:** Filter controls for:
  - Price range (min-max slider)
  - Location/area (dropdown/autocomplete)
  - Amenities (checkboxes)
  - Property type (radio buttons)
  - Rating (star selector)
  - Availability date range
  - Sort options (price, rating, newest)
- **Features:** Apply/reset filters, save filters

#### `pagination.html`
- **Purpose:** Navigation for paginated results
- **Contains:** 
  - Previous button
  - Page numbers
  - Next button
  - Items per page selector
  - Page info (showing X of Y results)

---

### Dashboard Templates: `dashboard/`

Currently empty - ready for implementation.

**Planned Templates:**
```
dashboard/
├── dashboard.html       # Main dashboard overview
├── my_bookings.html     # User's bookings history
├── my_listings.html     # User's posted listings (for landlords)
├── messages.html        # Chat/messaging interface
├── notifications.html   # Notifications center
├── saved_listings.html  # Bookmarked/favorite listings
├── my_reviews.html      # User's posted reviews
├── settings.html        # Dashboard settings
└── analytics.html       # Analytics (for landlords/admins)
```

---

## File Type Descriptions

### HTML Files (*.html)

- **`.html`** - Jinja2 templated HTML files used with Django
- **Dynamic Content:** Uses `{{ variable }}` for data injection
- **Template Tags:** Uses `{% if %}`, `{% for %}`, `{% include %}` etc.
- **Inheritance:** Can extend base.html with `{% extends "layouts/base.html" %}`

### CSS Files (*.css)

- **`.css`** - Cascading Style Sheets for styling
- **Organization:** Single main stylesheet with all styles
- **Responsive:** Media queries for mobile, tablet, desktop

### JavaScript Files (*.js)

- **`.js`** - Client-side scripting (currently empty)
- **Planned Use:** Form validation, dynamic filtering, modal handling, AJAX requests

---

## Key Features by Template Section

### Authentication Flow
```
Register (register.html) 
    ↓
Login (login.html) 
    ↓
Profile/Dashboard (profile.html, dashboard/*)
```

### Browsing & Booking Flow
```
Homepage (home/home.html)
    ↓
Search/Filter (home/search.html + boarding/filters.html)
    ↓
Listings (boarding/list.html)
    ↓
Details (boarding/details.html)
    ↓
Book (boarding/booking_form.html)
    ↓
Confirmation (dashboard/my_bookings.html)
    ↓
Review (boarding/reviews.html)
```

### Component Reusability

| Component | Used In | Times |
|-----------|---------|-------|
| `navbar.html` | base.html | Every page |
| `footer.html` | base.html | Every page |
| `card.html` | list.html, featured.html | Multiple |
| `filters.html` | list.html | Search pages |
| `pagination.html` | list.html | Multiple list views |
| `reviews.html` | details.html | Property details |

---

## Asset Organization

| Type | Location | Status |
|------|----------|--------|
| Stylesheets | `static/css/` | 1 main file |
| JavaScript | `static/js/` | Empty - ready |
| Images | `static/images/` | Empty - ready |
| User Uploads | `media/` | For uploaded content |

---

## Best Practices Used

✅ **Component-Based Design** - Reusable includes for navbar, footer, cards
✅ **Template Inheritance** - Single base.html for consistent layout
✅ **Semantic Structure** - Logical grouping by feature (accounts, boarding, etc.)
✅ **Separation of Concerns** - Static assets separate from templates
✅ **Scalability** - Easy to add new templates and components
✅ **Mobile-First** - CSS with responsive design approach

---

**Last Updated:** Documentation automatically generated from frontend structure
