# استخدم صورة أساسية لـ Python
FROM python:3.9-slim

# تعيين دليل العمل داخل الحاوية
WORKDIR /app

# نسخ ملف متطلبات التطبيق
COPY requirements.txt .

# تثبيت المكتبات المطلوبة
RUN pip install --no-cache-dir --timeout=120 -r requirements.txt


# نسخ باقي ملفات التطبيق (بما في ذلك app.py والنماذج)
COPY . .

# تعيين الأمر الافتراضي لتشغيل تطبيق Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8502", "--server.address=0.0.0.0"]
