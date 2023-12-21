# pip install PyPower

from numpy import array

from pypower.api import case30, runpf

# مثال یک سیستم با 30 گره
case_data = case30()

# افزودن یک خط انتقال
# اینجا بین گره 4 و 5 یک خط انتقال با ظرفیت 300 مگاوات افزوده شده است
case_data['branch'] = array([
   [4, 5, 0.0, 0.01, 0.0, 300.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
])

# اجرای تحلیل تراز ولتاژ
results, success = runpf(case_data)

# چاپ نتیجه
if success:
   print("تحلیل تراز ولتاژ با موفقیت انجام شد.")
   print(results['bus'][:, [0, 7]]) # چاپ ولتاژ گره‌ها
   print(results['branch'][:, [0, 1, 14]]) # چاپ جریان خطوط انتقال
else:
   print("تحلیل تراز ولتاژ با خطا مواجه شد.")
   print(results)