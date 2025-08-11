from django.core.management.base import BaseCommand
from portfolio.models import Profile, Course, BlogPost, PodcastEpisode, Category


class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Đang tạo dữ liệu mẫu...')

        # Tạo Profile
        profile, created = Profile.objects.get_or_create(
            name="Đào Huy Toàn",
            defaults={
                'tagline': 'Web Developer & Technology Enthusiast',
                'bio': '''Nice to meet you! My name is Toan and I am a person who is very passionate about technology, especially the web. I aspire to create websites that not only operate efficiently but also deliver significant practical value, featuring optimal design and exceptional user experiences. I continuously strive to learn and apply new technologies to improve my knowledge and build high-quality products that meet client needs. I look forward to meeting you!''',
                'email': 'duct1531@gmail.com',
                'phone': '0356581703',
                'facebook_url': 'https://facebook.com/daohuytoann',
                'youtube_url': 'https://youtube.com/@daohuytoann',
                'linkedin_url': 'https://linkedin.com/in/daohuytoann',
                'total_students': 0,
                'total_views': 0,
                'years_experience': 0,
                'courses_created': 5,
            }
        )
        self.stdout.write(f'✓ Profile: {profile.name}')

        # Tạo Categories
        categories_data = [
            {
                'name': 'Web Development',
                'description': 'Full-stack web applications và websites',
                'icon': 'fas fa-globe-americas',
                'color': '#007bff'
            },
            {
                'name': 'Mobile App',
                'description': 'Ứng dụng di động iOS và Android',
                'icon': 'fas fa-mobile-alt',
                'color': '#28a745'
            },
            {
                'name': 'Desktop App',
                'description': 'Ứng dụng desktop đa nền tảng',
                'icon': 'fas fa-desktop',
                'color': '#ffc107'
            },
            {
                'name': 'DevOps & Tools',
                'description': 'Automation tools và DevOps solutions',
                'icon': 'fas fa-tools',
                'color': '#dc3545'
            },
            {
                'name': 'Machine Learning',
                'description': 'AI và Machine Learning projects',
                'icon': 'fas fa-brain',
                'color': '#6f42c1'
            },
            {
                'name': 'Others',
                'description': 'Các project khác',
                'icon': 'fas fa-puzzle-piece',
                'color': '#6c757d'
            }
        ]
        
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(f'✓ Category: {category.name}')

        # Lấy categories để assign cho courses
        web_dev = Category.objects.get(name='Web Development')
        others = Category.objects.get(name='Others')

        # Tạo Courses/Projects
        courses_data = [
            {
                'title': 'E-Commerce Website',
                'description': 'Full-featured e-commerce website built with React.js, Node.js, and MongoDB. Includes shopping cart, payment integration, and admin dashboard.',
                'category': web_dev,
                'technologies': 'React.js, Node.js, MongoDB, Express.js, Stripe API',
                'level': 'advanced',
                'duration': 'In Development',
                'featured': True,
                'completed': False,
                'github_url': 'https://github.com/daohuytoann/ecommerce-project',
                'demo_url': '',
                'project_url': '',
            },
            {
                'title': 'Portfolio Website',
                'description': 'Personal portfolio website showcasing projects and skills. Built with modern web technologies including React and Tailwind CSS.',
                'category': web_dev,
                'technologies': 'Django, Bootstrap, JavaScript, SQLite',
                'level': 'intermediate',
                'duration': 'Completed',
                'featured': True,
                'completed': True,
                'github_url': 'https://github.com/daohuytoann/portfolio',
                'demo_url': 'https://daohuytoann.onrender.com',
                'project_url': '',
            },
            {
                'title': 'Task Management App',
                'description': 'A comprehensive task management application with real-time updates, user authentication, and collaborative features.',
                'category': web_dev,
                'technologies': 'React.js, Firebase, Material-UI, JavaScript',
                'level': 'intermediate',
                'duration': 'Completed',
                'featured': True,
                'completed': True,
                'github_url': 'https://github.com/daohuytoann/task-manager',
                'demo_url': '',
                'project_url': '',
            },
            {
                'title': 'Weather Dashboard',
                'description': 'Interactive weather dashboard with geolocation support, 7-day forecast, and beautiful data visualizations.',
                'category': web_dev,
                'technologies': 'HTML, CSS, JavaScript, OpenWeather API',
                'level': 'beginner',
                'duration': 'Completed',
                'featured': False,
                'completed': True,
                'github_url': 'https://github.com/daohuytoann/weather-app',
                'demo_url': '',
                'project_url': '',
            },
            {
                'title': 'Blog Platform',
                'description': 'Modern blog platform with CMS capabilities, user roles, and responsive design. Built with Django and Bootstrap.',
                'category': web_dev,
                'technologies': 'Django, Python, Bootstrap, SQLite, HTML, CSS',
                'level': 'intermediate',
                'duration': 'Completed',
                'featured': False,
                'completed': True,
                'github_url': 'https://github.com/daohuytoann/blog-platform',
                'demo_url': '',
                'project_url': '',
            },
        ]

        for course_data in courses_data:
            course, created = Course.objects.get_or_create(
                title=course_data['title'],
                defaults=course_data
            )
            self.stdout.write(f'✓ Course: {course.title}')

        # Tạo Blog Posts
        posts_data = [
            {
                'title': 'My Journey Into Web Development',
                'content': '''Starting my journey into web development has been one of the most rewarding decisions I've ever made. 
                From writing my first "Hello World" program to building complex web applications, every step has taught me something new.
                
                The learning curve was steep at first. Understanding concepts like HTML structure, CSS styling, and JavaScript functionality 
                seemed overwhelming. But with persistence and practice, these technologies became second nature.
                
                What I love most about web development is the constant evolution. There's always something new to learn, 
                whether it's a new framework, a better coding practice, or an innovative design pattern.
                
                My advice to anyone starting this journey: be patient with yourself, practice consistently, 
                and don't be afraid to build projects that challenge your current skill level.''',
                'tags': 'web development, career, programming, inspiration',
                'featured': True,
                'read_time': 6,
            },
            {
                'title': 'Why I Choose React for Frontend Development',
                'content': '''React has become my go-to library for building user interfaces, and here's why:
                
                1. Component-Based Architecture: Breaking down the UI into reusable components makes development more organized and maintainable.
                
                2. Virtual DOM: React's virtual DOM provides excellent performance optimization out of the box.
                
                3. Strong Ecosystem: The React ecosystem offers countless libraries and tools that speed up development.
                
                4. Job Market: React skills are highly sought after in the current job market.
                
                5. Learning Curve: While there's an initial learning curve, React's concepts are logical and well-documented.
                
                Whether you're building a simple portfolio or a complex web application, React provides the flexibility and tools needed to create amazing user experiences.''',
                'tags': 'react, frontend, javascript, web development',
                'featured': True,
                'read_time': 4,
            },
            {
                'title': 'Best Practices for Clean Code',
                'content': '''Writing clean, maintainable code is crucial for any developer. Here are some practices I follow:
                
                1. Use meaningful variable and function names that clearly describe their purpose.
                
                2. Keep functions small and focused on a single responsibility.
                
                3. Write comments for complex logic, but let the code speak for itself when possible.
                
                4. Follow consistent coding conventions throughout your project.
                
                5. Refactor regularly to improve code quality and remove technical debt.
                
                6. Use version control effectively with clear, descriptive commit messages.
                
                Remember, code is read more often than it's written. Make it easy for future you (and your teammates) to understand and modify.''',
                'tags': 'clean code, best practices, programming, development tips',
                'featured': False,
                'read_time': 5,
            },
        ]

        for post_data in posts_data:
            post, created = BlogPost.objects.get_or_create(
                title=post_data['title'],
                defaults=post_data
            )
            self.stdout.write(f'✓ Blog Post: {post.title}')

        # Tạo Podcast Episodes
        episodes_data = [
            {
                'title': 'Getting Started in Web Development',
                'description': '''In this first episode, I share my journey into web development. 
                From choosing the right technologies to building your first project, we cover the essentials 
                every beginner needs to know.''',
                'episode_number': 1,
                'duration': '28:45',
                'featured': True,
            },
            {
                'title': 'Frontend vs Backend: What to Choose?',
                'description': '''Exploring the differences between frontend and backend development. 
                Which path should you choose as a beginner? We discuss the pros and cons of each specialization 
                and how to make the right decision for your career.''',
                'episode_number': 2,
                'duration': '32:20',
                'featured': False,
            },
            {
                'title': 'Building Your Developer Portfolio',
                'description': '''Your portfolio is your ticket to landing that first job. In this episode, 
                we discuss what projects to include, how to showcase your skills effectively, 
                and common mistakes to avoid when building your developer portfolio.''',
                'episode_number': 3,
                'duration': '25:15',
                'featured': True,
            },
        ]

        for episode_data in episodes_data:
            episode, created = PodcastEpisode.objects.get_or_create(
                episode_number=episode_data['episode_number'],
                defaults=episode_data
            )
            self.stdout.write(f'✓ Podcast Episode: {episode.title}')

        self.stdout.write(self.style.SUCCESS('✅ Hoàn thành! Dữ liệu mẫu đã được tạo.'))
        self.stdout.write('🔑 Đăng nhập admin với: admin / admin (cần set password)')
        self.stdout.write('🌐 Truy cập: http://127.0.0.1:8000/') 