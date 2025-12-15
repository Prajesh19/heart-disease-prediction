# Deployment Guide for Heart Disease Prediction App

This guide covers multiple deployment options for your Flask application, from free hosting to cloud platforms.

## Pre-Deployment Checklist

Before deploying, make sure to:
- ✅ Test the application locally
- ✅ Ensure all dependencies are in `requirements.txt`
- ✅ Model files (`heart_model.pkl`, `scaler.pkl`) are included
- ✅ Set `debug=False` for production

---

## Option 1: Render (Recommended - Free & Easy)

**Render** offers free hosting with automatic SSL certificates.

### Steps:

1. **Create a Render Account**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub (recommended) or email

2. **Prepare Your Repository**
   - Push your code to GitHub
   - Make sure `requirements.txt` is in the root directory

3. **Create a New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name**: heart-disease-prediction (or your choice)
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Plan**: Free

4. **Add Environment Variables** (if needed)
   - Usually not required for this app

5. **Deploy**
   - Click "Create Web Service"
   - Render will build and deploy automatically
   - Your app will be available at `https://your-app-name.onrender.com`

### Note: Add gunicorn to requirements.txt
```bash
pip install gunicorn
```
Add `gunicorn` to your `requirements.txt` file.

---

## Option 2: Railway (Free Tier Available)

**Railway** is another excellent free hosting option.

### Steps:

1. **Sign up at Railway**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Configure**
   - Railway auto-detects Python apps
   - Add start command: `gunicorn app:app --bind 0.0.0.0:$PORT`
   - Or create a `Procfile` (see below)

4. **Deploy**
   - Railway automatically deploys on git push
   - Get your URL from the dashboard

---

## Option 3: Heroku (Requires Credit Card)

**Heroku** is a popular platform (free tier discontinued, but still popular).

### Steps:

1. **Install Heroku CLI**
   - Download from [heroku.com](https://devcenter.heroku.com/articles/heroku-cli)

2. **Create Procfile**
   Create a file named `Procfile` (no extension) in root:
   ```
   web: gunicorn app:app
   ```

3. **Login and Create App**
   ```bash
   heroku login
   heroku create your-app-name
   ```

4. **Deploy**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push heroku main
   ```

5. **Open App**
   ```bash
   heroku open
   ```

---

## Option 4: PythonAnywhere (Free Tier)

**PythonAnywhere** is great for Python apps.

### Steps:

1. **Sign up** at [pythonanywhere.com](https://www.pythonanywhere.com)

2. **Upload Files**
   - Use the Files tab to upload your project
   - Or use Git: `git clone https://github.com/yourusername/your-repo.git`

3. **Create Web App**
   - Go to Web tab
   - Click "Add a new web app"
   - Choose Flask
   - Select Python 3.10 (or latest)

4. **Configure WSGI File**
   - Edit the WSGI file:
   ```python
   import sys
   path = '/home/yourusername/Heart Disease Prediction'
   if path not in sys.path:
       sys.path.append(path)
   
   from app import app as application
   ```

5. **Reload** the web app

---

## Option 5: Google Cloud Platform (Free Tier)

### Steps:

1. **Install Google Cloud SDK**
   - Download from [cloud.google.com](https://cloud.google.com/sdk)

2. **Create App Engine App**
   ```bash
   gcloud app create
   ```

3. **Create app.yaml**
   Create `app.yaml` in root:
   ```yaml
   runtime: python39
   
   handlers:
   - url: /.*
     script: auto
   ```

4. **Deploy**
   ```bash
   gcloud app deploy
   ```

---

## Option 6: AWS Elastic Beanstalk

### Steps:

1. **Install EB CLI**
   ```bash
   pip install awsebcli
   ```

2. **Initialize**
   ```bash
   eb init -p python-3.9 heart-disease-app
   ```

3. **Create and Deploy**
   ```bash
   eb create heart-disease-env
   eb deploy
   ```

---

## Option 7: DigitalOcean App Platform

1. **Sign up** at [digitalocean.com](https://www.digitalocean.com)
2. **Create App** from GitHub
3. **Configure** build and run commands
4. **Deploy**

---

## Production Configuration

### Update app.py for Production

Make sure your `app.py` has:
```python
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Create .gitignore

Create `.gitignore`:
```
__pycache__/
*.pyc
*.pyo
*.pkl
.env
venv/
env/
.DS_Store
*.log
```

### Create Procfile (for Heroku/Railway)

Create `Procfile`:
```
web: gunicorn app:app --bind 0.0.0.0:$PORT
```

---

## Quick Start: Render Deployment

**Fastest way to deploy:**

1. **Add gunicorn to requirements.txt**
   ```bash
   echo "gunicorn==21.2.0" >> requirements.txt
   ```

2. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Ready for deployment"
   git remote add origin https://github.com/yourusername/your-repo.git
   git push -u origin main
   ```

3. **Deploy on Render**
   - Go to render.com
   - New Web Service
   - Connect GitHub repo
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app`
   - Deploy!

---

## Troubleshooting

### Common Issues:

1. **Module not found errors**
   - Ensure all dependencies are in `requirements.txt`
   - Check Python version compatibility

2. **Model files not found**
   - Make sure model files are committed to Git
   - Check file paths are relative (not absolute)

3. **Port binding errors**
   - Use `$PORT` environment variable
   - Or use `0.0.0.0` as host

4. **Static files not loading**
   - Ensure `static/` and `templates/` folders are in root
   - Check Flask static file configuration

---

## Recommended: Render (Easiest)

For beginners, **Render** is the easiest option:
- ✅ Free tier available
- ✅ Automatic SSL
- ✅ Easy GitHub integration
- ✅ No credit card required
- ✅ Simple configuration

---

## Need Help?

If you encounter issues:
1. Check the platform's logs
2. Verify all files are committed
3. Ensure `requirements.txt` is complete
4. Check that model files are included in the repository

Good luck with your deployment! 🚀

