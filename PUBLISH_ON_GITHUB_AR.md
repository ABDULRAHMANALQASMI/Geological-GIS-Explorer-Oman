# دليل رفع المشروع إلى GitHub ونشره على GitHub Pages

**اسم المستودع المقترح:** `Geological-GIS-Explorer-Oman`  
**المالك المتوقع:** `abdulrahmanalqasmi`، إذا كان هذا اسم حساب GitHub الذي ستستخدمه.  
**حالة المشروع:** ملفات جاهزة للرفع؛ **لم يتم رفعها إلى GitHub تلقائيًا**.

## أ. إنشاء مستودع جديد على GitHub

1. افتح https://github.com/new وسجّل الدخول.
2. اسم المستودع: `Geological-GIS-Explorer-Oman`.
3. اختر **Public** إذا كنت تريد استخدام GitHub Pages ضمن الحساب المجاني.
4. **لا** تفعّل خيارات إنشاء README أو `.gitignore` أو License أثناء إنشاء المستودع؛ لأن الملفات موجودة بالفعل.
5. اضغط **Create repository**.

## ب. رفع المشروع من VS Code (macOS)

1. فك ضغط حزمة GitHub الجاهزة إلى مجلد واضح.
2. في VS Code اختر **File → Open Folder** وحدد المجلد المحتوي على `index.html` مباشرة.
3. افتح **Terminal → New Terminal** وشغّل:

```bash
git init -b main
git add .
git commit -m "Publish Geological GIS Explorer Oman V4"
git remote add origin https://github.com/abdulrahmanalqasmi/Geological-GIS-Explorer-Oman.git
git push -u origin main
```

> عدّل اسم الحساب في رابط `origin` إذا كان حساب GitHub مختلفًا. تتطلب عملية `git push` تسجيل الدخول إلى GitHub في VS Code أو مدير الاعتماد؛ لا تستخدم كلمة مرور GitHub العادية في Terminal.

إذا ظهرت رسالة تطلب تعريف المؤلف عند أول commit، نفّذ `git config --global user.name "Abdulrahman Al Qasmi"` وأضف بريد GitHub المعتمد في `git config --global user.email "YOUR_GITHUB_EMAIL"` ثم أعد الأمر.

## ج. تفعيل GitHub Pages

1. افتح مستودع GitHub بعد الرفع.
2. اختر **Settings → Pages**.
3. تحت **Build and deployment** اختر **Deploy from a branch**.
4. اختر **main** ثم **/(root)** واضغط **Save**.
5. راجع تبويب **Actions** لمعرفة نتيجة النشر.

الموقع المتوقع إذا كان اسم الحساب هو المذكور:

https://abdulrahmanalqasmi.github.io/Geological-GIS-Explorer-Oman/

**مهم:** الرابط مجرد مسار متوقع، لا يعني أن الموقع منشور حاليًا.

## د. اختبار النشر

- تحقق من الصفحة الرئيسية وملفات CSS وJS.
- افتح الفهارس الطباقية وتأكد من تحميل JSON من `data/`.
- افتح خريطة GIS وتحقق من CDN وخدمات الصور الخارجية. لا تعمل بعض الخرائط دون إنترنت.
- افتح رابط البورتفوليو وجرّب الأزرار.
- تأكد من إشارة نجاح عملية `GEO-OMAN checks` في تبويب Actions.
- صفحة GitHub Pages **لا** تشغّل FastAPI أو PostgreSQL/PostGIS؛ تحتاج استضافة خلفية منفصلة.

## هـ. التحديثات اللاحقة

```bash
git add .
git commit -m "Update geology and GIS data"
git push
```

## طريقة بديلة عبر المتصفح

من صفحة المستودع اختر **Add file → Upload files**، ثم اسحب **محتويات** المجلد المفكوك (وليس ملف ZIP نفسه) وارفعها. قد يصعب رفع ملفات `.github` المخفية من بعض متصفحات macOS؛ استخدام VS Code وGit أفضل للحفاظ على الهيكل كاملًا.

## ملفات يُمنع نشرها

تجنب رفع ملفات خاصة، بيانات آبار غير مصرح بها، مفاتيح API، ملفات `.env`، سجلات شخصية، أو ملفات GeoTIFF خاصة دون التحقق من ترخيصها. `.gitignore` موجود لتقليل بعض مخاطر الرفع، لكنه لا يغني عن مراجعة المحتويات.
