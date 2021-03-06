#------------------------------------------------------------------------------
# test nek scripts
#
def test_readnek():
	import sys
	sys.path.append('./src/')
	import neksuite as ns

	fname = './tests/nek/channel3D_0.f00001'
	field = ns.readnek(fname)

	assert field.endian == 'little'
	assert field.istep  == 10
	assert field.lr1    == [8, 8, 8]
	assert field.ndim   == 3
	assert field.nel    == 512
	assert field.var    == [3, 3, 1, 0, 0]
	assert field.wdsz   == 4
	assert (field.time - 0.2) < 1e-3
	

def test_writenek():
	import sys
	sys.path.append('./src/')
	import neksuite as ns

	fname = './tests/nek/channel3D_0.f00001'
	field = ns.readnek(fname)

	fnamew = './test_0.f00001'
	status = ns.writenek(fnamew, field)
	
	assert status == 0
	
	fieldw = ns.readnek(fnamew)
	
	assert field.endian == fieldw.endian
	assert field.istep  == fieldw.istep
	assert field.lr1    == fieldw.lr1
	assert field.ndim   == fieldw.ndim
	assert field.nel    == fieldw.nel
	assert field.var    == fieldw.var
	assert field.wdsz   == fieldw.wdsz
	assert (field.time - fieldw.time) < 1e-3
	assert field.lims.pos.all()  == fieldw.lims.pos.all()
	assert field.lims.vel.all()  == fieldw.lims.vel.all()
	assert field.lims.pres.all() == fieldw.lims.pres.all()
	assert field.lims.scal.all() == fieldw.lims.scal.all()
	
	
def test_readrea():
	import sys
	sys.path.append('./src/')
	import neksuite as ns

	fname = './tests/nek/2D_section_R360.rea'
	field = ns.readrea(fname)

	assert field.lr1  == [2, 2, 1]
	assert field.ndim == 2
	assert field.nel  == 1248
	assert (field.elem[0].pos[0][0][0][0] - 0.048383219999999998 ) < 1e-3


def test_writerea():
	import sys
	sys.path.append('./src/')
	import neksuite as ns

	fname = './tests/nek/2D_section_R360.rea'
	field = ns.readrea(fname)

	fnamew = 'test.rea'
	status = ns.writerea(fnamew, field)

	assert status == 0

	fieldw = ns.readrea(fnamew)

	assert field.endian == fieldw.endian
	assert field.lr1    == fieldw.lr1
	assert field.ndim   == fieldw.ndim
	assert field.nel    == fieldw.nel
	assert field.wdsz   == fieldw.wdsz
	assert (field.elem[0].pos[0][0][0][0] - fieldw.elem[0].pos[0][0][0][0]) < 1e-3



#------------------------------------------------------------------------------
# test simson scripts
#
def test_readdns():
	import sys
	sys.path.append('./src/')
	import simsonsuite as ss

	fname = './tests/simson/channel3D_t10000v.u'
	field = ss.readdns(fname)

	assert field.endian == 'little'
	assert field.istep  == []
	assert field.lr1    == [48, 65, 48]
	assert field.ndim   == 3
	assert field.nel    == 1
	assert field.var    == [3, 3, 0, 0, 0]
	assert field.wdsz   == 8
	assert (field.time - 10000.439742009798) < 1e-3


def test_readplane():
	import sys
	sys.path.append('./src/')
	import simsonsuite as ss

	fname = './tests/simson/u.plane'
	x, d, nn, ndim = ss.readplane(fname)

	assert (x[0][1][0] - 0.06875) < 1e-3
	assert (d[0][1]    - 0.0034688727137604305) < 1e-3
	assert nn[0] == 97.
	assert nn[1] == 97.
	assert ndim  == 2

#==============================================================================
# run tests
#
if __name__ == "__main__":

	test_readnek()
	test_writenek()
	test_readrea()
	test_writerea()

	test_readdns()
	test_readplane()
