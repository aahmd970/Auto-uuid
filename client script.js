frappe.ui.form.on('Supplier', {
    before_save: function(frm) {
		if (!frm.doc.supplier_id) {
		    frappe.call({
		        method: "library_management.api.supplier_id_generation",
		        callback: function(response) {
                    frm.set_value('supplier_id', response.message);
                    refresh_field('supplier_id');
                }
		    })
		}
	}
})
