/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import kioskAttendanceApp from "@hr_attendance/public_kiosk/public_kiosk_app";

patch(kioskAttendanceApp.kioskAttendanceApp.prototype, {
    async kioskConfirm(employeeId){
		await super.kioskConfirm(employeeId);
		debugger;
		console.log("hihi");
	},
	async onManualSelection(employeeId, enteredPin){
		await super.onManualSelection(employeeId, enteredPin);
		debugger;
		console.log("hihi");
	}
});
