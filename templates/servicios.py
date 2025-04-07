<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Servicios - Silviagro S.A.S.</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
</head>
<body class="scroll-smooth bg-white text-gray-800 font-sans">

<header class="bg-white shadow-md fixed top-0 left-0 w-full z-50">
    <nav class="container mx-auto px-6 py-4 flex justify-between items-center">
        <h1 class="text-xl font-bold text-green-800 animate__animated animate__pulse animate__infinite">SILVIAGRO</h1>
        <button id="menu-toggle" class="md:hidden text-green-800 focus:outline-none">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
        </button>
        <ul id="menu" class="hidden md:flex md:space-x-8 flex-col md:flex-row absolute md:static top-16 left-0 w-full md:w-auto bg-white md:bg-transparent text-green-900 font-medium shadow-md md:shadow-none">
            <li><a href="/" class="block px-6 py-2 hover:text-green-700">Inicio</a></li>
            <li><a href="/#quehacemos" class="block px-6 py-2 hover:text-green-700">¿Qué hacemos?</a></li>
            <li><a href="#" class="block px-6 py-2 text-green-700 font-bold">Servicios</a></li>
            <li><a href="/#nosotros" class="block px-6 py-2 hover:text-green-700">Nosotros</a></li>
            <li><a href="/#contacto" class="block px-6 py-2 hover:text-green-700">Contacto</a></li>
        </ul>
    </nav>
</header>

<div class="h-28"></div>
<section class="p-6 sm:p-10 bg-green-100 min-h-screen scroll-mt-28" data-aos="fade-up">
    <h2 class="text-3xl font-bold text-center text-green-800 mb-10 animate__animated animate__fadeInUp">Nuestros Servicios</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8">
        <div class="h-80 bg-cover bg-center rounded-2xl shadow-xl border border-green-200 hover:shadow-2xl transition duration-300 flex flex-col justify-center p-6" style="background-image: url('/media/galeria/4.jpeg');">
            <h3 class="text-2xl font-bold text-white mb-2 drop-shadow-lg">Servicios Silviculturales</h3>
            <p class="text-white drop-shadow-md">
                Realizamos actividades silviculturales como siembra, poda, tala, traslado y tratamientos de árboles.
                Además, ofrecemos mantenimiento de jardines y corte de césped, garantizando espacios verdes saludables.
            </p>
        </div>

        <div class="h-80 bg-cover bg-center rounded-2xl shadow-xl border border-green-200 hover:shadow-2xl transition duration-300 flex flex-col justify-center p-6" style="background-image: url('/media/galeria/10.jpeg');">
            <h3 class="text-2xl font-bold text-white mb-2 drop-shadow-lg">Servicios Agropecuarios</h3>
            <p class="text-white drop-shadow-md">
                Desarrollo de actividades agropecuarias integrales: producción, transformación, exportación, importación
                y comercialización de productos agrícolas y pecuarios. Apoyamos el desarrollo rural con prácticas sostenibles.
            </p>
        </div>

        <div class="h-80 bg-cover bg-center rounded-2xl shadow-xl border border-green-200 hover:shadow-2xl transition duration-300 flex flex-col justify-center p-6" style="background-image: url('/media/galeria/21.jpeg');">
            <h3 class="text-2xl font-bold text-white mb-2 drop-shadow-lg">Avalújos Rurales y Urbanos</h3>
            <p class="text-white drop-shadow-md">
                Realizamos avalújos técnicos, económicos y legales de predios rurales y urbanos bajo normativas vigentes,
                garantizando confianza en procesos de compra, venta o inversión.
            </p>
        </div>

        <div class="h-80 bg-cover bg-center rounded-2xl shadow-xl border border-green-200 hover:shadow-2xl transition duration-300 flex flex-col justify-center p-6" style="background-image: url('/media/galeria/28.jpeg');">
            <h3 class="text-2xl font-bold text-white mb-2 drop-shadow-lg">Servicios Complementarios</h3>
            <p class="text-white drop-shadow-md">
                Ejecutamos todas las actividades conexas, complementarias o relacionadas con nuestro objeto social,
                que faciliten el desarrollo legal y comercial de nuestras operaciones.
            </p>
        </div>
    </div>
</section>

<footer class="bg-green-100 py-6 mt-10 relative z-10">
    <div class="container mx-auto px-6 flex flex-col md:flex-row justify-between items-center text-center text-green-800 text-sm space-y-4 md:space-y-0 md:space-x-8">
        <div class="flex items-center space-x-2">
            <span>📞</span> 
            <a href="tel:+573107391584" class="hover:underline font-semibold">310 739 1584</a>
            <span>|</span>
            <a href="tel:+573165319026" class="hover:underline font-semibold">316 531 9026</a>
        </div>
        <div class="flex items-center space-x-2">
            <span>✉️</span>
            <a href="mailto:silviagrosascol@gmail.com" class="hover:underline font-semibold">silviagrosascol@gmail.com</a>
        </div>
        <div class="flex items-center space-x-2">
            <span>📍</span>
            <span class="font-semibold">Calle 19 #3-10 oficina 701</span>
        </div>
    </div>
</footer>

<a href="#" class="fixed bottom-24 left-6 bg-gradient-to-r from-green-500 to-lime-500 hover:from-lime-500 hover:to-green-700 text-white p-3 rounded-full shadow-lg hover:shadow-xl z-50 transition-all duration-300">
    ⬆️
</a>

<a href="https://wa.me/573107391584" target="_blank" class="fixed bottom-24 right-6 bg-gradient-to-r from-green-500 to-emerald-500 hover:from-lime-500 hover:to-green-700 text-white p-4 rounded-full shadow-lg z-50 transition-all duration-300">
    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 fill-current" viewBox="0 0 24 24">
        <path d="M20.52 3.48A12.001 12.001 0 0 0 3.48 20.52a12.043 12.043 0 0 0 5.09 3.02l.52.14 1.51-5.41a7.477 7.477 0 0 1-3.05-2.98l-.35-.59 2.29-.76c.25-.08.52-.13.79-.13.62 0 1.24.18 1.77.52l.5.33 2.77-.92a7.57 7.57 0 0 1 1.01-2.78 7.466 7.466 0 0 1 5.01-2.99z"/>
    </svg>
</a>

<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
<script>AOS.init();</script>
<script>
    const toggle = document.getElementById('menu-toggle');
    const menu = document.getElementById('menu');
    toggle.addEventListener('click', () => {
        menu.classList.toggle('hidden');
    });
</script>

</body>
</html>