from flask_assets import Bundle

#any custom css
app_css = Bundle(
    'app.css',
    output='styles/app.css')

#any custom js
app_js = Bundle(
    'app.js',
    filters='jsmin',
    output='scripts/app.js')

#all vendor specific css
vendor_css = Bundle(
    'vendor/bootstrap.min.css',
    'vendor/owl.carousel.css',
    'vendor/font-awesome.min.css',
    'vendor/owl.theme.default.css',
    output='styles/vendor.css')

#all vendor specific js
vendor_js = Bundle(
    'vendor/jquery.min.js',
    'vendor/bootstrap.min.js',
    'vendor/jquery.stellar.min.js',
    'vendor/owl.carousel.min.js',
    'vendor/zxcvbn.js',
    filters='jsmin',
    output='scripts/vendor.js')
