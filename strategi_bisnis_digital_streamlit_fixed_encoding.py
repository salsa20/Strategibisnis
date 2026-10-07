# -*- coding: utf-8 -*-
import streamlit as st

st.set_page_config(page_title='Strategi Bisnis Digital', page_icon='💼', layout='wide')

st.markdown('''<style>
.main-title{font-size:2.35rem;font-weight:800}.subtitle{color:#667085;font-size:1.05rem}
.card{padding:1rem;border:1px solid #e4e7ec;border-radius:12px;margin-bottom:.7rem;background:#fff}
.case{padding:1rem;border-left:5px solid #4f46e5;border-radius:10px;background:#f7f9fc}
.term{padding:.65rem .8rem;border:1px solid #e5e7eb;border-radius:9px;margin-bottom:.5rem;background:#f8fafc}
</style>''', unsafe_allow_html=True)

# Sumber utama: Patnaik et al. (Eds.). 2019. Digital Business: Business Algorithms,
# Cloud Computing and Data Engineering. Springer. DOI 10.1007/978-3-319-93940-7
# Referensi pendukung: Bharadwaj et al. (2013), Vial (2019), Verhoef et al. (2021),
# Warner & Wäger (2019), serta Nanda, S. Patnaik & S. Patnaik (2019).

MODULES = {
'1. Fondasi Strategi Bisnis Digital': {
'objective': ['Menjelaskan digital business dan digital business strategy.','Membedakan digitization, digitalization, dan digital transformation.','Menganalisis perubahan penciptaan dan penangkapan nilai.','Menganalisis scope, scale, speed, dan value creation/capture.'],
'concept': '''## 1.1 Digital Business
**Bisnis digital (digital business)** adalah cara organisasi menggunakan teknologi digital, data, dan konektivitas untuk menjalankan, mengembangkan, atau mengubah aktivitas bisnis dan penciptaan nilai.

Patnaik et al. (2019) membahas digital business melalui transformasi bisnis, cloud computing, IoT, mobile platforms, big data, data mining, business intelligence, dan algorithmic business.

## 1.2 Digital Business Strategy
**Digital business strategy** menghubungkan keputusan bisnis dengan kemampuan digital untuk menciptakan dan menangkap nilai. Bharadwaj et al. (2013) menekankan empat dimensi: **scope** (cakupan), **scale** (skala), **speed** (kecepatan), serta **value creation and capture** (penciptaan dan penangkapan nilai).

## 1.3 Tiga istilah penting
**Digitization** = mengubah informasi analog menjadi format digital, misalnya kertas menjadi PDF.

**Digitalization** = menggunakan teknologi digital untuk memperbaiki proses yang sudah ada, misalnya stok manual menjadi sistem inventori digital.

**Digital transformation** = perubahan strategis yang lebih mendasar terhadap cara organisasi menciptakan, memberikan, dan menangkap nilai melalui teknologi digital, proses, organisasi, dan model bisnis.

Ketiganya jangan disamakan: digitization berfokus pada data, digitalization pada proses, sedangkan digital transformation pada perubahan bisnis yang lebih menyeluruh.''',
'terms': [
('Digital Business','Aktivitas bisnis yang memanfaatkan teknologi digital, data, dan konektivitas untuk menciptakan atau menyampaikan nilai.'),
('Digital Business Strategy','Strategi bisnis yang menyatukan keputusan bisnis dengan kemampuan digital untuk menciptakan dan menangkap nilai.'),
('Digitization','Konversi informasi analog menjadi format digital.'),
('Digitalization','Pemanfaatan teknologi digital untuk meningkatkan proses atau aktivitas yang sudah ada.'),
('Digital Transformation','Perubahan strategis dan organisasi yang mengubah cara perusahaan menciptakan, memberikan, dan menangkap nilai dengan teknologi digital.'),
('Value Creation','Proses menciptakan manfaat atau nilai bagi pelanggan/pihak terkait.'),
('Value Capture','Cara perusahaan memperoleh manfaat ekonomi dari nilai yang diciptakan.'),
('Digital Ecosystem','Jaringan perusahaan, pelanggan, platform, pemasok, dan teknologi yang saling terhubung dalam penciptaan nilai digital.')],
'case': '''### Studi Kasus 1 - Toko Retail Tradisional
Sebuah toko pakaian menerima pesanan melalui WhatsApp dan marketplace, tetapi stok masih dicatat manual. Pemilik ingin menggunakan teknologi digital, tetapi belum tahu apakah perlu membangun aplikasi sendiri.

**Pertanyaan:**
1. Apakah toko tersebut sudah dapat disebut digital business?
2. Mana yang termasuk digitization dan digitalization?
3. Apakah membangun aplikasi sendiri merupakan prioritas?
4. Analisis dengan scope, scale, speed, dan value creation/capture.
5. Tentukan 3 KPI.

**Arah diskusi:** mulai dari masalah bisnis, kebutuhan pelanggan, proses, data, dan nilai; jangan langsung memilih teknologi.''',
'exercise':['Buat tabel digitization vs digitalization vs digital transformation, masing-masing dua contoh.','Pilih satu UMKM dan identifikasi satu masalah yang dapat diselesaikan dengan teknologi digital.','Buat peta masalah bisnis -> data -> teknologi -> perubahan proses -> nilai bisnis.']},

'2. Algorithmic Business dan Data-Driven Decision': {
'objective':['Menjelaskan algorithmic business.','Membedakan data, informasi, insight, dan keputusan.','Mengidentifikasi penggunaan algoritma dalam proses bisnis.','Menganalisis manfaat dan risiko keputusan berbasis algoritma.'],
'concept': '''## 2.1 Algorithmic Business
Bab **Towards Algorithmic Business: A Paradigm Shift in Digital Business** menjelaskan penggunaan algoritma untuk menghasilkan insight, mendukung proses, layanan pelanggan, analisis data, dan pengambilan keputusan bisnis.

**Algoritma** adalah serangkaian langkah atau aturan sistematis untuk menghasilkan output dari input tertentu.

Contoh: histori pembelian -> algoritma segmentasi -> segmen pelanggan -> keputusan promosi.

## 2.2 Data -> Informasi -> Insight -> Keputusan
**Data** = fakta/catatan mentah.

**Informasi** = data yang telah diberi konteks melalui pengolahan.

**Insight** = pemahaman dari analisis yang membantu menjawab apa yang terjadi, mengapa, atau apa yang sebaiknya dilakukan.

**Decision** = tindakan/pilihan berdasarkan insight, tujuan, batasan, dan risiko.

## 2.3 Contoh algoritma bisnis
Recommendation, classification, forecasting, optimization, dan anomaly detection.

## 2.4 Risiko
Algoritma dapat meningkatkan kecepatan, skala, dan konsistensi, tetapi tetap bergantung pada kualitas data. Risiko mencakup bias, explainability, privasi, governance, dan ketergantungan berlebihan pada model.''',
'terms':[('Algorithm','Serangkaian langkah/aturan sistematis untuk mengubah input menjadi output.'),('Algorithmic Business','Pemanfaatan algoritma dalam insight, proses, layanan, analisis, dan keputusan bisnis.'),('Data-Driven Decision','Keputusan yang menggunakan data dan hasil analisis sebagai dasar utama.'),('Recommendation System','Sistem yang memberikan rekomendasi item yang relevan bagi pengguna.'),('Classification','Teknik menetapkan data ke kelas/kategori tertentu.'),('Forecasting','Perkiraan nilai atau kondisi masa depan berdasarkan data historis.'),('Optimization','Pencarian solusi terbaik berdasarkan tujuan dan batasan.'),('Anomaly Detection','Proses menemukan observasi atau pola yang tidak biasa.'),('Bias','Kecenderungan sistem/data menghasilkan hasil yang tidak netral.'),('Data Governance','Kebijakan, peran, aturan, dan proses untuk memastikan data dikelola secara tepat dan dapat dipertanggungjawabkan.')],
'case':'''### Studi Kasus 2 - Marketplace dan Rekomendasi Produk
Marketplace memiliki histori pembelian, pencarian, kategori produk, harga, waktu transaksi, dan interaksi pengguna. Manajemen ingin meningkatkan conversion rate melalui rekomendasi personal.

**Pertanyaan:**
1. Apa input, proses, dan output sistem rekomendasi?
2. Algoritma apa yang dapat digunakan secara konseptual?
3. KPI apa yang digunakan?
4. Apa risiko jika histori transaksi mengandung bias?
5. Bagaimana menjaga rekomendasi tetap relevan bagi pelanggan?

**Output:** Data -> preprocessing -> algorithm -> recommendation -> customer response -> KPI -> improvement.''',
'exercise':['Buat contoh algorithmic business dari pendidikan, perbankan, retail, atau kesehatan.','Tentukan input, proses, output, keputusan, dan KPI.','Identifikasi tiga risiko data/algoritma dan mitigasinya.']},

'3. Cloud Computing sebagai Infrastruktur Strategis': {
'objective':['Menjelaskan cloud computing.','Membedakan IaaS, PaaS, dan SaaS.','Memahami cloud sebagai pendukung scalability dan elasticity.','Memilih pendekatan cloud berdasarkan kebutuhan bisnis.'],
'concept': '''## 3.1 Cloud Computing
**Cloud computing** adalah model penyediaan sumber daya komputasi melalui jaringan sehingga organisasi dapat menggunakan compute, storage, database, platform, atau software secara fleksibel.

## 3.2 Model layanan
**IaaS (Infrastructure as a Service)** menyediakan infrastruktur seperti virtual machine, storage, dan network.

**PaaS (Platform as a Service)** menyediakan lingkungan untuk mengembangkan dan menjalankan aplikasi.

**SaaS (Software as a Service)** menyediakan software siap pakai sebagai layanan.

## 3.3 Konsep strategis
**Scalability** = kemampuan meningkatkan kapasitas ketika beban tumbuh.

**Elasticity** = kemampuan menyesuaikan kapasitas terhadap perubahan beban secara dinamis.

Cloud dapat mendukung fleksibilitas, kecepatan pengembangan, availability, dan kolaborasi. Namun cloud tidak otomatis selalu lebih murah; keputusan harus mempertimbangkan biaya, keamanan, regulasi, integrasi, performa, dan kemampuan tim.''',
'terms':[('Cloud Computing','Penyediaan sumber daya komputasi melalui jaringan secara fleksibel sesuai kebutuhan.'),('IaaS','Layanan infrastruktur seperti server virtual, storage, dan jaringan.'),('PaaS','Platform/lingkungan untuk mengembangkan dan menjalankan aplikasi.'),('SaaS','Software siap pakai yang diakses sebagai layanan.'),('Scalability','Kemampuan meningkatkan kapasitas untuk menangani pertumbuhan beban.'),('Elasticity','Kemampuan menyesuaikan kapasitas mengikuti perubahan beban.'),('Availability','Tingkat kesiapan sistem untuk dapat digunakan ketika dibutuhkan.'),('Workload','Beban kerja komputasi yang harus diproses sistem.'),('Infrastructure','Komponen dasar seperti server, jaringan, storage, dan compute.'),('Cloud Migration','Proses memindahkan aplikasi, data, atau workload ke cloud.')],
'case':'''### Studi Kasus 3 - Aplikasi Pemesanan Makanan
Aplikasi memiliki 5.000 transaksi/hari pada kondisi normal, tetapi saat promosi beban meningkat berkali-kali lipat. Server lokal sering mendekati batas kapasitas.

**Pertanyaan:**
1. Mengapa scalability dan elasticity penting?
2. Apakah seluruh sistem harus langsung dipindahkan ke cloud?
3. Kapan IaaS, PaaS, atau SaaS lebih relevan?
4. Risiko apa yang perlu diperhatikan?
5. Apa KPI teknologi dan KPI bisnis yang harus dipantau?

**Tugas:** buat rekomendasi arsitektur konseptual beserta alasan bisnis dan teknis.''',
'exercise':['Buat tabel IaaS, PaaS, SaaS.','Pilih model cloud untuk tiga skenario berbeda dan jelaskan alasannya.','Buat daftar KPI availability, latency, cost, utilization, dan business KPI.']},

'4. Data Engineering dan Business Intelligence': {
'objective':['Menjelaskan peran data engineering.','Memahami alur data dari sumber sampai dashboard/keputusan.','Membedakan ETL dan ELT.','Menghubungkan data engineering dengan business intelligence.'],
'concept': '''## 4.1 Data Engineering
**Data engineering** adalah praktik membangun sistem dan pipeline agar data dikumpulkan, dipindahkan, dibersihkan, disimpan, dan tersedia untuk analisis.

Sumber dapat berupa transaksi, aplikasi, website, IoT, media sosial, CRM, dan ERP.

## 4.2 Data Pipeline
Alur sederhana:
**Data Source -> Ingestion -> Storage -> Transformation -> Warehouse/Lake -> BI/Analytics -> Decision**

**Data ingestion** = memasukkan data ke sistem.
**Transformation** = membersihkan, mengubah, menggabungkan, atau membuat variabel.
**Data warehouse** = penyimpanan data terstruktur untuk analitik.
**Data lake** = penyimpanan data besar dengan format lebih beragam.

## 4.3 ETL dan ELT
**ETL** = Extract -> Transform -> Load; transformasi dilakukan sebelum loading.

**ELT** = Extract -> Load -> Transform; data dimuat dahulu lalu ditransformasi di platform tujuan.

Pilihan tergantung volume, arsitektur, platform, governance, dan kebutuhan analitik.

## 4.4 Business Intelligence
**BI** menggunakan data dan analitik untuk menghasilkan informasi bagi monitoring dan pengambilan keputusan bisnis.''',
'terms':[('Data Engineering','Praktik membangun sistem dan pipeline agar data tersedia, berkualitas, dan siap digunakan.'),('Data Pipeline','Rangkaian proses perpindahan dan pengolahan data dari sumber sampai tujuan.'),('Data Ingestion','Proses mengambil/memasukkan data ke sistem.'),('ETL','Extract-Transform-Load; transformasi dilakukan sebelum loading.'),('ELT','Extract-Load-Transform; data dimuat lalu ditransformasi.'),('Data Warehouse','Penyimpanan data terstruktur yang dioptimalkan untuk analitik.'),('Data Lake','Penyimpanan data skala besar dengan format yang beragam.'),('Business Intelligence','Pemanfaatan data dan analitik untuk menghasilkan informasi bagi keputusan.'),('Data Quality','Tingkat ketepatan, kelengkapan, konsistensi, validitas, dan keterandalan data.'),('Dashboard','Antarmuka visual yang menyajikan KPI dan informasi penting.')],
'case':'''### Studi Kasus 4 - Retail Omnichannel
Perusahaan memiliki transaksi toko fisik, marketplace, website, data pelanggan, dan data promosi. Format berbeda dan dashboard penjualan sering tidak sama dengan laporan keuangan.

**Pertanyaan:**
1. Apa masalah data engineering yang mungkin terjadi?
2. Buat rancangan data pipeline.
3. Kapan ETL atau ELT dapat dipilih?
4. Apa dimensi data quality yang perlu diperiksa?
5. KPI apa yang perlu ada di dashboard manajemen?

**Output:** diagram arsitektur data + penjelasan fungsi tiap tahap.''',
'exercise':['Gambarkan pipeline transaksi sampai dashboard.','Berikan contoh masalah data quality pada retail.','Bandingkan ETL dan ELT berdasarkan lokasi transformasi, fleksibilitas, dan komputasi.']},

'5. IoT, Mobility, Platform, dan Ekosistem Digital': {
'objective':['Menjelaskan peran IoT dan mobile technology.','Memahami platform dan digital ecosystem.','Menganalisis network effects.','Merancang strategi digital berbasis ekosistem.'],
'concept': '''## 5.1 Internet of Things
**IoT** adalah konsep menghubungkan objek/perangkat dengan jaringan sehingga perangkat dapat mengirim, menerima, atau bertukar data.

Nilai bisnis IoT tidak hanya berasal dari sensor, tetapi dari data dan keputusan yang dapat diperbaiki.

## 5.2 Mobile Technology
Teknologi mobile memperluas titik kontak pelanggan dan memungkinkan interaksi serta pengumpulan data secara kontekstual.

## 5.3 Digital Platform
**Digital platform** adalah infrastruktur digital yang memfasilitasi interaksi atau transaksi antar kelompok pengguna.

## 5.4 Network Effect
**Network effect** terjadi ketika nilai platform berubah karena jumlah/aktivitas pengguna berubah.

**Direct network effect**: nilai meningkat karena bertambahnya pengguna pada sisi yang sama.

**Cross-side network effect**: pertumbuhan satu kelompok meningkatkan nilai bagi kelompok lain.

Platform harus memperhatikan governance, trust, quality, incentives, data, pricing, dan user experience.''',
'terms':[('IoT','Jaringan perangkat/objek yang terhubung dan dapat menghasilkan atau bertukar data.'),('Sensor','Komponen yang menangkap kondisi/fenomena dan mengubahnya menjadi data.'),('Mobile Technology','Teknologi yang memungkinkan layanan dan interaksi melalui perangkat bergerak.'),('Digital Platform','Infrastruktur digital yang memfasilitasi interaksi/transaksi antar pihak.'),('Digital Ecosystem','Jaringan aktor dan teknologi yang saling bergantung dalam penciptaan nilai.'),('Network Effect','Perubahan nilai layanan akibat perubahan jumlah/aktivitas pengguna dalam jaringan.'),('Direct Network Effect','Nilai meningkat karena bertambahnya pengguna pada sisi yang sama.'),('Cross-Side Network Effect','Nilai satu kelompok dipengaruhi pertumbuhan kelompok lain.'),('Platform Governance','Aturan dan mekanisme untuk mengatur interaksi, kualitas, keamanan, dan perilaku platform.'),('Omnichannel','Pendekatan yang mengintegrasikan berbagai kanal pelanggan agar pengalaman dan data lebih konsisten.')],
'case':'''### Studi Kasus 5 - Platform Lokal untuk UMKM
Platform ingin menghubungkan UMKM makanan, pelanggan, dan kurir lokal. Masalah awal: sedikit UMKM, sedikit pelanggan, kurir belum tertarik, pelanggan khawatir kualitas, dan data masih sedikit.

**Pertanyaan:**
1. Siapa aktor dalam ekosistem?
2. Apa value proposition tiap pihak?
3. Network effect apa yang mungkin terjadi?
4. Bagaimana memulai saat pengguna masih sedikit?
5. Bagaimana governance menjaga kualitas dan trust?
6. Dari mana sumber pendapatan?

**Output:** rancangan ekosistem digital dan penjelasan penciptaan serta penangkapan nilai.''',
'exercise':['Gambarkan minimal tiga aktor digital ecosystem.','Buat value proposition untuk tiap aktor.','Identifikasi direct dan cross-side network effect pada platform.']},

'6. Data, Social Media, Customer Experience, dan Strategi Digital': {
'objective':['Menjelaskan peran data dan social media.','Menghubungkan customer journey dengan data digital.','Menggunakan KPI digital untuk evaluasi strategi.','Menyusun rekomendasi strategi digital berbasis kasus.'],
'concept': '''## 6.1 Social Media
Social media bukan hanya kanal promosi. Dalam strategi digital, media sosial dapat menjadi kanal komunikasi, sumber feedback, sumber data interaksi, ruang komunitas, dan kanal customer service.

## 6.2 Customer Journey
**Customer journey** adalah rangkaian pengalaman pelanggan dari mengenal produk, mempertimbangkan, membeli, menggunakan, sampai membeli ulang atau merekomendasikan.

Contoh: **Awareness -> Consideration -> Purchase -> Use -> Retention/Advocacy**.

## 6.3 KPI Digital
**Reach** = jumlah akun/orang yang terpapar.
**Engagement rate** = tingkat interaksi terhadap basis audiens tertentu.
**CTR** = rasio klik terhadap impression/click opportunity sesuai definisi pengukuran.
**Conversion rate** = proporsi pengguna yang melakukan tindakan target.
**CAC** = biaya rata-rata memperoleh pelanggan baru.
**Retention rate** = proporsi pelanggan yang bertahan dalam periode tertentu.
**CLV/LTV** = estimasi nilai ekonomi pelanggan selama hubungan dengan bisnis.

Jangan menjadikan vanity metrics sebagai satu-satunya dasar keputusan.

## 6.4 Strategi Digital Berbasis Data
**Business Goal -> Customer Problem -> Data -> Analysis -> Insight -> Action -> KPI -> Review**

Strategi digital yang baik menjelaskan mengapa kanal, data, teknologi, dan aktivitas dipilih untuk mencapai tujuan.''',
'terms':[('Customer Journey','Rangkaian pengalaman pelanggan dari awareness sampai penggunaan, retensi, atau advokasi.'),('Awareness','Tahap ketika calon pelanggan mulai mengetahui produk/merek.'),('Engagement','Interaksi pengguna dengan konten, produk, atau kanal digital.'),('Conversion','Perubahan pengguna menjadi melakukan tindakan target.'),('CTR','Click-Through Rate; rasio klik terhadap jumlah kesempatan tayang sesuai definisi.'),('Conversion Rate','Rasio pengguna yang melakukan tindakan target dibanding basis pengguna.'),('CAC','Customer Acquisition Cost; biaya rata-rata memperoleh pelanggan baru.'),('Retention Rate','Proporsi pelanggan yang tetap bertahan pada periode tertentu.'),('CLV/LTV','Estimasi nilai ekonomi pelanggan sepanjang hubungan dengan perusahaan.'),('Vanity Metric','Metrik yang terlihat positif tetapi belum tentu menunjukkan dampak bisnis nyata.')],
'case':'''### Studi Kasus 6 - Kampanye Digital Produk Lokal
Brand makanan lokal meningkatkan followers 40%, tetapi penjualan hanya naik 3%. Impressions, engagement, dan website traffic meningkat, namun conversion rate rendah dan banyak pelanggan baru tidak melakukan pembelian ulang.

**Pertanyaan:**
1. Apakah kampanye berhasil?
2. Metrik mana yang berpotensi menjadi vanity metric?
3. Pada tahap customer journey mana masalah kemungkinan terjadi?
4. Data apa yang perlu diperiksa?
5. Strategi apa untuk meningkatkan conversion dan retention?
6. Bagaimana mengukur keberhasilan strategi baru?

**Output:** Goal -> Problem -> Data -> Insight -> Action -> KPI.''',
'exercise':['Hitung conversion rate jika 10.000 pengunjung menghasilkan 250 pembelian.','Sebutkan tiga KPI yang lebih dekat dengan dampak bisnis daripada followers.','Buat customer journey untuk satu produk lokal.']}
}

QUIZ=[
('Perubahan dokumen kertas menjadi PDF paling tepat disebut...', ['Digitization','Digitalization','Digital transformation','Digital ecosystem'], 'Digitization','Digitization adalah konversi informasi analog menjadi format digital.'),
('Manakah yang paling tepat menggambarkan algorithmic business?', ['Menggunakan algoritma untuk mendukung insight, proses, layanan, atau keputusan bisnis','Mengganti semua pegawai dengan robot','Menggunakan media sosial hanya untuk promosi','Menyimpan seluruh data tanpa analisis'], 'Menggunakan algoritma untuk mendukung insight, proses, layanan, atau keputusan bisnis','Algorithmic business memanfaatkan algoritma untuk insight dan aktivitas/keputusan bisnis.'),
('Layanan cloud yang menyediakan software siap digunakan disebut...', ['IaaS','PaaS','SaaS','IoT'], 'SaaS','SaaS menyediakan software sebagai layanan.'),
('Pada ETL, transformasi data dilakukan...', ['Sebelum data dimuat ke target','Setelah data dimuat ke target','Hanya setelah dashboard dibuat','Hanya pada perangkat IoT'], 'Sebelum data dimuat ke target','ETL berarti Extract, Transform, Load.'),
('Kemampuan menyesuaikan kapasitas mengikuti perubahan beban secara dinamis disebut...', ['Elasticity','Digitization','Governance','Conversion'], 'Elasticity','Elasticity mengacu pada penyesuaian kapasitas terhadap perubahan workload.'),
('Contoh cross-side network effect adalah...', ['Bertambahnya pembeli membuat platform lebih menarik bagi penjual','Mengubah Word menjadi PDF','Menambah RAM satu komputer','Mengganti warna logo'], 'Bertambahnya pembeli membuat platform lebih menarik bagi penjual','Pertumbuhan satu kelompok pengguna meningkatkan nilai bagi kelompok lain.'),
('CAC digunakan untuk mengukur...', ['Biaya rata-rata memperoleh pelanggan baru','Jumlah pelanggan yang bertahan','Jumlah tayangan iklan','Kecepatan server'], 'Biaya rata-rata memperoleh pelanggan baru','CAC adalah Customer Acquisition Cost.'),
('Jika 10.000 pengunjung menghasilkan 250 pembelian, conversion rate adalah...', ['0,25%','2,5%','25%','40%'], '2,5%','250 / 10.000 x 100% = 2,5%.'),
('Urutan analisis strategi digital yang paling tepat adalah...', ['Business Goal -> Customer Problem -> Data -> Analysis -> Insight -> Action -> KPI','Technology -> Technology -> Technology -> KPI','Followers -> Followers -> Followers -> Revenue','Dashboard -> Logo -> Website -> Data'], 'Business Goal -> Customer Problem -> Data -> Analysis -> Insight -> Action -> KPI','Strategi dimulai dari tujuan dan masalah bisnis lalu menggunakan data untuk menghasilkan tindakan dan evaluasi.'),
('Pernyataan paling tepat tentang cloud computing adalah...', ['Cloud selalu lebih murah daripada lokal','Cloud dapat mendukung fleksibilitas dan skalabilitas, tetapi keputusan harus mempertimbangkan biaya, keamanan, regulasi, dan kebutuhan bisnis','Cloud hanya untuk penyimpanan file','Cloud tidak membutuhkan governance'], 'Cloud dapat mendukung fleksibilitas dan skalabilitas, tetapi keputusan harus mempertimbangkan biaya, keamanan, regulasi, dan kebutuhan bisnis','Cloud mendukung fleksibilitas, tetapi bukan berarti selalu paling murah atau bebas risiko.')
]



# ============================================================
# 10 KASUS DISKUSI KELOMPOK
# ============================================================
DISCUSSION_CASES = [
    {"title":"Kelompok 1 - Toko Retail Tradisional","topic":"Fondasi Strategi Bisnis Digital","case":"Sebuah toko pakaian memiliki omzet yang relatif stabil. Transaksi dilakukan di toko fisik. Pemilik mulai menerima pesanan melalui WhatsApp dan marketplace, tetapi stok masih dicatat manual. Pemilik ingin menggunakan teknologi digital, tetapi belum tahu apakah harus langsung membangun aplikasi sendiri.","questions":["Apakah kondisi toko tersebut sudah dapat disebut digital business?","Mana yang termasuk digitization dan mana yang termasuk digitalization?","Apakah membangun aplikasi sendiri merupakan prioritas strategis?","Bagaimana teknologi digital dapat menciptakan dan menangkap nilai?","Tentukan 3 KPI untuk mengevaluasi strategi."]},
    {"title":"Kelompok 2 - Marketplace dan Rekomendasi Produk","topic":"Algorithmic Business dan Data-Driven Decision","case":"Sebuah marketplace memiliki jutaan histori transaksi. Manajemen ingin meningkatkan conversion rate dengan menampilkan rekomendasi produk personal. Data yang tersedia meliputi histori pembelian, pencarian, kategori produk, harga, waktu transaksi, dan interaksi pengguna.","questions":["Apa input, proses, dan output dari sistem rekomendasi?","Algoritma apa yang secara konseptual dapat digunakan?","KPI apa yang digunakan untuk mengevaluasi keberhasilan?","Apa risiko jika histori transaksi mengandung bias?","Bagaimana perusahaan memastikan rekomendasi tetap relevan bagi pelanggan?"]},
    {"title":"Kelompok 3 - Aplikasi Pemesanan Makanan","topic":"Cloud Computing sebagai Infrastruktur Strategis","case":"Sebuah perusahaan kuliner memiliki aplikasi pemesanan. Pada hari biasa terdapat sekitar 5.000 transaksi per hari, tetapi saat promosi jumlah transaksi dapat meningkat berkali-kali lipat. Sistem lama menggunakan server lokal yang kapasitasnya terbatas.","questions":["Mengapa scalability dan elasticity penting pada kasus ini?","Apakah perusahaan harus langsung memindahkan seluruh sistem ke cloud?","Kapan IaaS, PaaS, atau SaaS lebih relevan?","Risiko apa yang harus diperhatikan?","KPI teknologi dan KPI bisnis apa yang perlu dipantau?"]},
    {"title":"Kelompok 4 - Retail Omnichannel dan Data Terfragmentasi","topic":"Data Engineering dan Business Intelligence","case":"Perusahaan retail memiliki transaksi dari toko fisik, marketplace, website, data pelanggan, dan data promosi. Setiap sumber menggunakan format berbeda. Dashboard penjualan sering menunjukkan angka yang tidak sama dengan laporan keuangan.","questions":["Apa masalah data engineering yang mungkin terjadi?","Buat rancangan data pipeline sederhana dari sumber data sampai dashboard.","Kapan ETL atau ELT dapat dipilih?","Apa saja aspek data quality yang harus diperiksa?","KPI apa yang sebaiknya tersedia untuk manajemen?"]},
    {"title":"Kelompok 5 - Platform Lokal untuk UMKM","topic":"Platform dan Digital Ecosystem","case":"Sekelompok mahasiswa ingin membuat platform yang menghubungkan UMKM makanan, pelanggan, dan kurir lokal. Masalah awal: sedikit UMKM, sedikit pelanggan, kurir belum tertarik bergabung, pelanggan khawatir kualitas produk, dan platform belum memiliki data yang cukup.","questions":["Siapa saja aktor dalam digital ecosystem?","Apa value proposition untuk masing-masing pihak?","Network effect apa yang mungkin terjadi?","Bagaimana platform memulai ketika pengguna masih sedikit?","Bagaimana governance menjaga kualitas dan kepercayaan?","Dari mana sumber pendapatan platform?"]},
    {"title":"Kelompok 6 - Kampanye Digital Produk Lokal","topic":"Customer Experience dan Strategi Digital","case":"Sebuah brand makanan lokal menghabiskan anggaran untuk iklan media sosial. Jumlah followers meningkat 40%, tetapi penjualan hanya naik 3%. Impressions, engagement, dan website traffic meningkat, tetapi conversion rate relatif rendah dan sebagian besar pelanggan baru tidak melakukan pembelian ulang.","questions":["Apakah kampanye tersebut dapat disebut berhasil?","Metrik mana yang berpotensi menjadi vanity metric?","Pada tahap customer journey mana masalah kemungkinan terjadi?","Data apa yang perlu diperiksa lebih lanjut?","Strategi apa yang dapat dilakukan untuk meningkatkan conversion dan retention?","Bagaimana mengukur keberhasilan strategi baru?"]},
    {"title":"Kelompok 7 - Bank Digital dan Onboarding Nasabah","topic":"Digital Transformation dan Customer Experience","case":"Sebuah bank digital mengalami banyak calon nasabah yang berhenti ketika proses pembukaan rekening. Data menunjukkan traffic aplikasi tinggi, tetapi completion rate onboarding rendah. Tim bisnis mengusulkan menambah promosi, sedangkan tim produk menduga proses verifikasi identitas terlalu panjang.","questions":["Apa masalah bisnis utama yang perlu dipastikan terlebih dahulu?","Data apa yang perlu dianalisis untuk memahami titik pelanggan berhenti?","Bagaimana customer journey dapat digunakan untuk menemukan bottleneck?","Apakah menambah promosi merupakan solusi yang tepat? Jelaskan.","Rancang minimal 4 KPI untuk mengevaluasi perbaikan onboarding.","Apa risiko keamanan dan privasi yang harus diperhatikan?"]},
    {"title":"Kelompok 8 - Smart Warehouse Berbasis IoT","topic":"IoT, Data Engineering, dan Operational Analytics","case":"Perusahaan distribusi sering mengalami kesalahan stok dan keterlambatan pengiriman. Manajemen ingin memasang sensor IoT untuk memantau posisi barang, suhu gudang, dan aktivitas keluar-masuk barang secara real time. Namun biaya investasi dan integrasi dengan sistem lama menjadi perhatian.","questions":["Masalah bisnis apa yang sebenarnya ingin diselesaikan?","Data apa yang perlu dikumpulkan oleh sensor?","Bagaimana alur data dari sensor sampai dashboard operasional?","Apa manfaat dan risiko penggunaan IoT?","Bagaimana membandingkan manfaat bisnis dengan biaya investasi?","Tentukan KPI operasional dan KPI bisnis yang relevan."]},
    {"title":"Kelompok 9 - Fintech dan Credit Scoring","topic":"Algorithmic Business, Data, dan Risk Management","case":"Sebuah fintech menggunakan data transaksi dan perilaku digital untuk membantu menilai kelayakan kredit. Model mampu mempercepat keputusan, tetapi ditemukan bahwa tingkat persetujuan berbeda cukup besar antar kelompok pelanggan. Manajemen harus menentukan apakah model tetap digunakan, diperbaiki, atau diganti.","questions":["Apa manfaat algorithmic decision-making pada kasus ini?","Data dan variabel apa yang perlu diaudit?","Mengapa bias model dapat menjadi masalah bisnis dan etika?","Bagaimana perusahaan menguji performa dan fairness model?","Apa bentuk governance yang perlu diterapkan?","Buat rekomendasi keputusan dan KPI pemantauannya."]},
    {"title":"Kelompok 10 - UMKM Go Digital tetapi Profit Tidak Naik","topic":"Strategi Bisnis Digital dan Value Capture","case":"Sebuah UMKM makanan telah masuk marketplace, menggunakan media sosial, menerima pembayaran digital, dan menjalankan iklan online. Penjualan meningkat 20%, tetapi laba hampir tidak berubah karena biaya promosi, komisi platform, diskon, dan biaya operasional juga meningkat.","questions":["Mengapa peningkatan penjualan belum tentu berarti strategi digital berhasil?","Bedakan value creation dan value capture pada kasus tersebut.","Data biaya dan pendapatan apa yang perlu dianalisis?","KPI apa yang sebaiknya digunakan selain omzet?","Alternatif strategi apa yang dapat meningkatkan profitabilitas?","Buat rekomendasi strategi digital yang mempertimbangkan pelanggan dan keberlanjutan bisnis."]},
]

st.sidebar.title('Strategi Bisnis Digital')
st.sidebar.caption('Case Method Learning App')
page=st.sidebar.radio('Navigasi',['Beranda','Materi','Studi Kasus','Latihan','Kuis','Glosarium','Referensi'])

if page=='Beranda':
    st.markdown('<div class="main-title">Strategi Bisnis Digital</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Materi berbasis studi kasus: strategi, algoritma, cloud, data engineering, platform, IoT, dan customer experience.</div>', unsafe_allow_html=True)
    a,b,c=st.columns(3); a.metric('Modul',len(MODULES)); b.metric('Kuis',len(QUIZ)); c.metric('Metode','Case Method')
    st.markdown('## Capaian Pembelajaran')
    st.markdown('''Setelah mengikuti materi, mahasiswa diharapkan mampu:
- menjelaskan istilah utama bisnis digital;
- menganalisis dampak teknologi digital terhadap proses dan model bisnis;
- memilih teknologi berdasarkan masalah bisnis, bukan sekadar tren;
- menganalisis algoritma, cloud, data engineering, IoT, platform, dan social media;
- menyusun rekomendasi strategi digital berbasis data dan KPI.''')
    st.markdown('## Alur Case Method')
    cols=st.columns(5)
    for col,n,t,d in zip(cols,['1','2','3','4','5'],['Case','Identify','Analyze','Decide','Reflect'],['Baca kasus','Identifikasi masalah','Gunakan konsep/data','Susun alternatif','Evaluasi KPI']):
        col.markdown(f'<div class="card"><b>{n}. {t}</b><br>{d}</div>',unsafe_allow_html=True)
    st.info('Prinsip utama: mulai dari tujuan bisnis, masalah pelanggan, proses, data, dan nilai; bukan langsung dari teknologi.')

elif page=='Materi':
    st.title('Materi Kuliah')
    selected=st.selectbox('Pilih modul',list(MODULES))
    m=MODULES[selected]
    st.markdown('## Tujuan Pembelajaran')
    for x in m['objective']: st.markdown('- '+x)
    st.divider(); st.markdown(m['concept']); st.divider(); st.markdown('## Istilah Penting')
    for t,meaning in m['terms']: st.markdown(f'<div class="term"><b>{t}</b><br>{meaning}</div>',unsafe_allow_html=True)

elif page=='Studi Kasus':
    st.title('Tugas Diskusi Studi Kasus')
    st.caption('10 kelompok • 1 kasus per kelompok • Case Method')
    selected_idx=st.selectbox('Pilih kelompok/kasus',range(len(DISCUSSION_CASES)),format_func=lambda i: DISCUSSION_CASES[i]['title'])
    item=DISCUSSION_CASES[selected_idx]
    st.markdown(f"## {item['title']}")
    st.markdown(f"**Topik:** {item['topic']}")
    st.markdown('<div class="case">',unsafe_allow_html=True)
    st.markdown('### Situasi Kasus')
    st.write(item['case'])
    st.markdown('</div>',unsafe_allow_html=True)
    st.markdown('## Pertanyaan Diskusi')
    for i,q in enumerate(item['questions'],1): st.markdown(f'**{i}.** {q}')
    st.divider()
    st.markdown('## Format Output Kelompok')
    st.markdown("""
**1. Identifikasi masalah bisnis** - Jelaskan masalah utama berdasarkan fakta kasus.

**2. Analisis** - Gunakan konsep materi untuk menjelaskan penyebab dan kondisi kasus.

**3. Alternatif solusi** - Susun minimal dua alternatif.

**4. Evaluasi alternatif** - Bandingkan manfaat, biaya, risiko, kebutuhan data, teknologi, dan dampaknya terhadap pelanggan.

**5. Rekomendasi** - Pilih satu alternatif dan berikan alasan yang logis.

**6. KPI** - Tentukan indikator untuk mengukur keberhasilan rekomendasi.

**7. Risiko dan mitigasi** - Identifikasi risiko utama dan cara menguranginya.
""")
    st.info('Setiap kelompok sebaiknya mempertahankan hubungan yang jelas antara masalah -> data -> konsep -> alternatif -> rekomendasi -> KPI.')

elif page=='Latihan':
    st.title('Latihan')
    selected=st.selectbox('Pilih modul latihan',list(MODULES))
    for i,item in enumerate(MODULES[selected]['exercise'],1):
        st.markdown(f'### Latihan {i}'); st.write(item); st.text_area('Jawaban:',key=f'ex_{selected}_{i}',height=100)
    st.markdown('### Tantangan Integratif')
    st.code('Business Goal -> Customer Problem -> Data Needed -> Digital Technology -> Process Change -> Value Creation -> KPI -> Risk & Mitigation')

elif page=='Kuis':
    st.title('Kuis Pemahaman')
    answers=[]
    for i,(q,opts,ans,exp) in enumerate(QUIZ):
        answers.append(st.radio(f'{i+1}. {q}',opts,index=None,key=f'q{i}'))
    if st.button('Periksa Nilai',type='primary'):
        score=sum(a==item[2] for a,item in zip(answers,QUIZ) if a is not None)
        unanswered=sum(a is None for a in answers)
        st.success(f'Skor: {score}/{len(QUIZ)} ({score/len(QUIZ)*100:.0f}%)')
        if unanswered: st.warning(f'{unanswered} soal belum dijawab.')
        st.markdown('## Pembahasan')
        for i,item in enumerate(QUIZ):
            with st.expander(f'Soal {i+1}'): st.write('**Jawaban:** '+item[2]); st.write(item[3])

elif page=='Glosarium':
    st.title('Glosarium Strategi Bisnis Digital')
    terms={}
    for m in MODULES.values():
        for t,meaning in m['terms']: terms[t]=meaning
    s=st.text_input('Cari istilah')
    for t in sorted(terms):
        if s.lower() in t.lower() or s.lower() in terms[t].lower():
            st.markdown(f'<div class="term"><b>{t}</b><br>{terms[t]}</div>',unsafe_allow_html=True)

elif page=='Referensi':
    st.title('Referensi')
    st.markdown('''### Sumber utama
**Patnaik, S., Yang, X.-S., Tavana, M., Popentiu-Vlădicescu, F., & Qiao, F. (Eds.). (2019).** *Digital Business: Business Algorithms, Cloud Computing and Data Engineering.* Springer. DOI: https://doi.org/10.1007/978-3-319-93940-7

### Referensi ilmiah pendukung
- Bharadwaj, A., El Sawy, O. A., Pavlou, P. A., & Venkatraman, N. (2013). *Digital Business Strategy: Toward a Next Generation of Insights*. MIS Quarterly, 37(2), 471-482. DOI: https://doi.org/10.25300/MISQ/2013/37:2.3
- Vial, G. (2019). *Understanding digital transformation: A review and a research agenda*. The Journal of Strategic Information Systems, 28(2). DOI: https://doi.org/10.1016/j.jsis.2019.01.003
- Verhoef, P. C. et al. (2021). *Digital transformation: A multidisciplinary reflection and research agenda*. Journal of Business Research, 122, 889-901. DOI: https://doi.org/10.1016/j.jbusres.2019.09.022
- Warner, K. S. R., & Wäger, M. (2019). *Building dynamic capabilities for digital transformation*. Long Range Planning, 52(3), 326-349. DOI: https://doi.org/10.1016/j.lrp.2018.12.001
- Nanda, P., Patnaik, S., & Patnaik, S. (2019). *Towards Algorithmic Business: A Paradigm Shift in Digital Business*. In Digital Business, pp. 3-22. Springer. DOI: https://doi.org/10.1007/978-3-319-93940-7_1''')
    st.info('Struktur materi mengikuti empat bagian utama buku Patnaik et al.: Digital Business Transformation, Cloud Computing, IoT & Mobility, serta Information Management & Social Media; konsep strategi diperkuat dengan literatur ilmiah pendukung.')

st.sidebar.divider(); st.sidebar.caption('Materi kuliah • Case Method • Strategi Bisnis Digital')
