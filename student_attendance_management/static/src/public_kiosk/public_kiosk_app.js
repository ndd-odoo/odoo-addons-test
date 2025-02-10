/** @odoo-module **/

import { registry } from "@web/core/registry";
import { patch } from "@web/core/utils/patch";
import kiosk from "@hr_attendance/public_kiosk/public_kiosk_app";


patch(kiosk.kioskAttendanceApp.prototype, {
	setup(){
		super.setup();
		debugger;
	},

    async onBarcodeScanned(barcode) {
        console.log("📌 Scanning Barcode:", barcode);
        if (this.lockScanner || this.state.active_display !== 'main') {
            return;
        }
        this.lockScanner = true;

        let badgeId = barcode;
        let courseId = null;

        if (barcode.includes('_')) {
            [badgeId, courseId] = barcode.split('_');
        }

        console.log("🔹 Extracted Badge ID:", badgeId);
        console.log("🔹 Extracted Course ID:", courseId);

        const result = await this.rpc('/hr_attendance/attendance_barcode_scanned', {
            'barcode': badgeId,
            'token': this.props.token,
            'course_id': courseId
        });

        if (result && result.employee_name) {
            this.employeeData = result;
            this.switchDisplay('greet');
        } else {
            this.displayNotification(_t("No employee found for Badge ID '%(badgeId)s' and Course ID '%(courseId)s'", { badgeId, courseId }));
        }

        this.lockScanner = false;
    }
});
