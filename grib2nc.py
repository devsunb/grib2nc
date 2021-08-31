import pygrib

from grib2nc.util.nc import NCWriter

grib = pygrib.open('/mnt/e/project/grib2nc/data/20190601-20190630.grib')

dt_dict = {}

for m in grib.read():
    dt = m.validDate.strftime('%Y%m%d%H%M%S')
    if dt in dt_dict:
        dt_dict[dt].append(m)
    else:
        dt_dict[dt] = [m]

for dt in dt_dict:
    nc = NCWriter('/mnt/e/project/grib2nc/data/ERA5_AN_MET_{}.nc'.format(dt))
    if dt_dict[dt]:
        lat, lon = dt_dict[dt][0].latlons()
        shape = lat.shape
        nc.create_dimension('number_of_lines', shape[0])
        nc.create_dimension('pixels_per_line', shape[1])
        nc.create_variable('/latitude', lat)
        nc.create_variable('/longitude', lon)
    for m in dt_dict[dt]:
        name = m.name
        data = m.values
        shape = data.shape
        nc.create_dimension('number_of_lines', shape[0])
        nc.create_dimension('pixels_per_line', shape[1])
        nc.create_variable('/{}'.format(name), data)
    nc.close()
