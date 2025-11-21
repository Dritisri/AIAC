# Portfolio Website

A modern, responsive portfolio website built with HTML, CSS, and JavaScript.

## 🌟 Features

### Design
- **Modern Color Palette**: Rich blues and purples with professional gradients
- **Typography**: Clean, readable fonts (Inter for body, Poppins for headings)
- **Dark Theme**: Eye-friendly dark background with vibrant accents

### Layout & Responsive Design
- **Grid Layout**: CSS Grid for responsive project cards
- **Flexbox**: Flexible navigation and content alignment
- **Mobile-First**: Fully responsive design for all devices
- **Mobile Menu**: Hamburger menu for mobile navigation

### Navigation
- **Smooth Scrolling**: Seamless navigation between sections
- **Active Links**: Current section highlighting
- **Fixed Navbar**: Always accessible navigation
- **Scroll Indicator**: Visual scroll prompt on homepage

### Sections
1. **Home**: Hero section with introduction and call-to-action
2. **About Me**: Personal introduction with skills showcase
3. **Projects**: Portfolio of your work with project cards
4. **Contact**: Contact form and social media links

## 📁 File Structure

```
Lab-14/
│
├── index.html      # Main HTML structure
├── styles.css      # All styling and responsive design
├── script.js       # Navigation and interactive features
├── README.md       # This file
└── Task-1.py       # Original file
```

## 🚀 Getting Started

### Option 1: Direct Browser Opening
1. Simply open `index.html` in your web browser
2. The website will work offline

### Option 2: Local Server (Recommended)
1. Install a local server (e.g., VS Code Live Server extension)
2. Open the project folder
3. Right-click `index.html` and select "Open with Live Server"

## 🎨 Customization

### Colors
Edit the CSS variables in `styles.css`:
```css
:root {
    --primary-color: #6366f1;    /* Main color */
    --primary-light: #818cf8;    /* Light accent */
    --bg-color: #0f172a;         /* Background */
    --text-primary: #f8fafc;     /* Text color */
}
```

### Content
1. **Personal Information**: Update name, title, and description in `index.html`
2. **About Section**: Modify the about text in the About Me section
3. **Projects**: Add your projects in the Projects section
4. **Contact Info**: Update email, phone, and location in Contact section

### Images
Replace the SVG placeholders with your actual images:
- Add your photo in the About section
- Replace project image placeholders with your project screenshots

## 📱 Responsive Breakpoints

- **Desktop**: 1200px and above
- **Tablet**: 768px - 1199px
- **Mobile**: Below 768px

## ✨ Key Features Explained

### Smooth Scrolling
The navigation uses JavaScript to smoothly scroll to sections when clicking nav links.

### Active Section Detection
The current section is automatically highlighted as you scroll through the page.

### Scroll Animations
Elements fade in as they come into view using the Intersection Observer API.

### Form Validation
The contact form includes basic validation to ensure all fields are filled.

## 🛠️ Technologies Used

- **HTML5**: Semantic markup
- **CSS3**: Modern styling with CSS Variables, Grid, Flexbox
- **JavaScript (ES6+)**: Interactive functionality
- **SVG**: Placeholder graphics

## 📝 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## 🎯 Future Enhancements

Potential additions you could make:
- Backend integration for the contact form
- Blog section
- Animation library integration (e.g., GSAP)
- Light/dark mode toggle
- Multi-language support
- Analytics integration

## 📄 License

Free to use and modify for personal and commercial projects.

## 👤 Author

Your Name - Web Developer & Creative Designer

---

**Note**: Remember to update all placeholder content with your actual information before deploying!
