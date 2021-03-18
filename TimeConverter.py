def timeConverter(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%02d:%02d:%02d" % (hour, minutes, seconds)
      
detik = input("Masukkan detik: ")

if detik.strip().isdigit() and int(detik) <= 359999:
  print("Konversi :" + timeConverter(int(detik)))
elif int(detik) >= 359999 or int(detik) == " ":
  print("Invalid input!")
else:
  print("Invalid input!")
