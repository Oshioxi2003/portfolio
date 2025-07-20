# 🎨 Theme & Language Switching System

## 🌟 **Features Implemented**

### ✅ **1. Theme Switching (Dark/Light Mode)**

**Dark Theme (Default):**
- Background: `#111111`
- Secondary: `#1e1e1e`
- Text: `#ffffff`
- Borders: `#333333`

**Light Theme:**
- Background: `#ffffff`
- Secondary: `#f8f9fa`
- Text: `#333333`
- Borders: `#e9ecef`

**Toggle Control:**
- **Position:** Top-right corner
- **Icon:** Sun (dark mode) / Moon (light mode)
- **Storage:** localStorage
- **Transition:** Smooth 0.3s animations

### ✅ **2. Language Switching (Vietnamese/English)**

**Supported Languages:**
- **English (EN)** - Default
- **Vietnamese (VI)**

**Content Translated:**
- Navigation menu
- Page titles
- Button labels
- Form placeholders
- Static text content
- Personal information labels

**Toggle Control:**
- **Position:** Top-right corner (next to theme)
- **Display:** EN/VI indicator
- **Storage:** localStorage
- **Real-time:** Instant content switching

## 🎛️ **Controls Usage**

### **Theme Switcher:**
```html
<!-- Located at top-right corner -->
<div class="theme-switcher" onclick="toggleTheme()">
    <i class="fas fa-sun" id="theme-icon"></i>
</div>
```

### **Language Switcher:**
```html
<!-- Located next to theme switcher -->
<div class="lang-switcher" onclick="toggleLanguage()">
    <span id="lang-text">EN</span>
</div>
```

## 🔧 **Implementation Details**

### **CSS Variables System:**
```css
:root {
    --primary-color: #ffb400;
    /* Theme variables dynamically set */
}

[data-theme="dark"] {
    --bg-color: var(--dark-bg);
    --text-color: var(--dark-text);
    /* etc... */
}

[data-theme="light"] {
    --bg-color: var(--light-bg);
    --text-color: var(--light-text);
    /* etc... */
}
```

### **JavaScript Translation System:**
```javascript
const translations = {
    'vi': {
        'home': 'Trang chủ',
        'about': 'Giới thiệu',
        // ... all Vietnamese translations
    },
    'en': {
        'home': 'Home',
        'about': 'About',
        // ... all English translations
    }
};
```

### **HTML Data Attributes:**
```html
<!-- For content translation -->
<h1 data-translate="about_me">ABOUT ME</h1>

<!-- For form placeholders -->
<input data-translate-placeholder="name_placeholder" />
```

## 🚀 **How to Use**

### **1. Toggle Theme:**
- Click the sun/moon icon in top-right corner
- Theme preference saved automatically
- All colors change smoothly

### **2. Toggle Language:**
- Click the EN/VI indicator next to theme switcher
- Language preference saved automatically
- All text content updates instantly

### **3. Persistence:**
- Settings saved in localStorage
- Automatically restored on page reload
- Works across all pages

## 📱 **Responsive Design**

**Mobile Support:**
- Switchers remain accessible on all screen sizes
- Touch-friendly 45px buttons
- No overlap with content

**Desktop Experience:**
- Hover effects with scaling
- Smooth transitions
- Clear visual feedback

## 🎨 **Theme Customization**

**Light Theme Colors:**
```css
--light-bg: #ffffff
--light-secondary: #f8f9fa
--light-text: #333333
--light-text-muted: #666666
--light-border: #e9ecef
```

**Dark Theme Colors:**
```css
--dark-bg: #111111
--dark-secondary: #1e1e1e
--dark-text: #ffffff
--dark-text-muted: #999999
--border-color: #333333
```

## 🌐 **Translation Content**

### **Vietnamese Translations:**
- Navigation: Trang chủ, Giới thiệu, Dự án, Liên hệ
- Home: Personal greeting and bio in Vietnamese
- Forms: Vietnamese placeholders
- Buttons: Vietnamese action labels

### **English Translations:**
- Navigation: Home, About, Projects, Contact
- Home: Professional English content
- Forms: English placeholders
- Buttons: English action labels

## 🔧 **Technical Features**

### **Performance:**
- ✅ CSS Variables for instant theme switching
- ✅ Minimal JavaScript footprint
- ✅ No page reloads required
- ✅ Smooth animations

### **Accessibility:**
- ✅ Clear visual contrast in both themes
- ✅ Proper focus states
- ✅ Screen reader friendly
- ✅ Keyboard navigation support

### **Browser Support:**
- ✅ Modern browsers (Chrome, Firefox, Safari, Edge)
- ✅ CSS Variables support
- ✅ localStorage support
- ✅ Smooth transitions

## 🎯 **User Experience**

### **Immediate Feedback:**
- Theme changes instantly
- Language switches without delay
- Visual indicators for current state
- Smooth hover effects

### **Intuitive Controls:**
- Recognizable sun/moon icons
- Clear EN/VI language indicators
- Consistent positioning
- Easy to find and use

## 📂 **Files Modified**

### **Templates:**
- `base.html` - Theme CSS, switchers, JavaScript
- `home.html` - Translation attributes
- `about.html` - Translation attributes
- `contact.html` - Translation attributes
- `courses.html` - Translation attributes

### **Forms:**
- `portfolio/forms.py` - Placeholder attributes

### **Styling:**
- All CSS updated to use CSS variables
- Responsive switcher positioning
- Smooth transition effects

## 🎉 **Ready to Use!**

**Test the Features:**
1. **Theme Switching:** Click sun/moon icon
2. **Language Switching:** Click EN/VI indicator
3. **Persistence:** Reload page to see saved preferences
4. **Responsive:** Test on different screen sizes

**Both systems work seamlessly together for the best user experience!** 🌟 