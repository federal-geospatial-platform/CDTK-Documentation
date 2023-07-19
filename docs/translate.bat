sphinx-build -b gettext source/. build/gettext -c source/conf

sphinx-intl update -p build/gettext -l fr -d source/locale
