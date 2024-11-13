
berat_badan=float(input('masukan berat badan anda :'))
tinggi_badan=float(input('Masukan tinggi badan anda :'))
rumus_bmi=   berat_badan / tinggi_badan

if rumus_bmi < 18.5 :
    status='Berat badan Kurang'
elif 18.5 <= 24.9:
    status='Berat badan normal'
elif 25 <= rumus_bmi <29.9:
    status='Kelebihan berat badan'
elif rumus_bmi>=30:
    status='Obesitas'
print(berat_badan)
print(tinggi_badan)
print(rumus_bmi)
print(f'anda memiliki status:{status}')
