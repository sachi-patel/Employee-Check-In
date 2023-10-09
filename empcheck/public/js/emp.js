frappe.ui.form.on("Employee Checkin", {
    onload :function(frm) {
		function onPositionRecieved(position){
			var long= position.coords.longitude;
			var lat= position.coords.latitude;
			frm.set_value('longitude',long);
			frm.set_value('latitude',lat);
			console.log("long",frm.doc.longitude);
			console.log("lat",frm.doc.latitude);
			
			
		}
		
		function locationNotRecieved(positionError){
			console.log(positionError);
		}
		
		
			if(navigator.geolocation){
				navigator.geolocation.getCurrentPosition(onPositionRecieved,locationNotRecieved,{ enableHighAccuracy: true});
			}
		
            frappe.db.get_doc('Employee',frm.doc.employee).then((r) => {
               
            const emp_latitude = r.latitude; 
            const emp_longitude = r.longitude; 
    
            const checkin_latitude = frm.doc.latitude;
            const checkin_longitude = frm.doc.longitude;
    
            //Haversine formula 
            const distance = haversineDistance(emp_latitude, emp_longitude, checkin_latitude, checkin_longitude);
    
           
            if (distance > 1) {
                frm.set_value('location_status', 'Fail');
            } else {
                frm.set_value('location_status', 'Success');
            }
    
            // Update the "Map" field
            frm.set_value('map', `Latitude: ${checkin_latitude}, Longitude: ${checkin_longitude}`);
        })
        }
    });
    
    function haversineDistance(lat1, lon1, lat2, lon2) {
        const R = 6371; // Radius of the Earth
        const dLat = deg2rad(lat2 - lat1);
        const dLon = deg2rad(lon2 - lon1);
        const a =
            Math.sin(dLat / 2) * Math.sin(dLat / 2) +
            Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) *
            Math.sin(dLon / 2) * Math.sin(dLon / 2);
        const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        const distance = R * c; 
        return distance;
    }
    
    function deg2rad(deg) {
        return deg * (Math.PI / 180);
    }
		
