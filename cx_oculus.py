import viz, oculus
hmd = oculus.Rift()

from tools import laser_pointer
laser = laser_pointer.LaserPointer()

from ray_caster import RayCaster
ray = ray_caster.RayCaster()

def link( view = viz.MainView ):
	sensor = hmd.getSensor()
	transport = viz.addGroup()
	viewLink = viz.link( transport, view )	
	viewLink.preMultLinkable( sensor )
	laserLink( viewLink, laser )
	profile = hmd.getProfile()
	if profile:
		viewLink.setOffset( [ 0, profile.eyeHeight, 0 ] )
	else:
		viewLink.setOffset( [ 0, 1.8, 0 ] )
		
	data = {
		'Device': 'Oculus',
		'Name': 'View',
		'Position': str( transport.getPosition() ),
		'Rotation': str( viewLink.getEuler() ),
		'Scale': '(0.0, 0.0, 0.0)',
		'Description': '',
		'Object': ''
	}
	
	return data

	



	