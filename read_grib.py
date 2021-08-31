import pygrib

grib = pygrib.open('/mnt/e/project/grib2nc/data/20190601-20190630.grib')

dt_dict = {}

for m in grib.read():
    dt = m.validDate.strftime('%Y%m%d%H%M%S')
    if dt in dt_dict:
        dt_dict[dt].append(m)
    else:
        dt_dict[dt] = [m]

for dt in dt_dict:
    for m in dt_dict[dt]:
        name = m.name
        data = m.values
        print(dt, m)
        print(data)
        print()
