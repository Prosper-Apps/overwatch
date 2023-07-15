// Copyright (c) 2023, Flexcom Systems and contributors
// For license information, please see license.txt

frappe.ui.form.on('Site Setup', {
    refresh: function(frm) {
        frm.add_custom_button('Create Site', function() {
            frappe.call({
                method: 'overwatch.overwatch.doctype.site_setup.site_setup.create_site',
                args: { 
                    'agent_url': frm.doc.agent_url, 
                    'site_name': frm.doc.site_name, 
                    'db_root_password': frm.doc.db_root_password,  // replace with the actual password
                    'admin_password': frm.doc.admin_password,  // replace with the actual password
                },
                callback: function(response) {
                    if(response.message.status == "error") {
                        frappe.msgprint(__('Site creation failed: ') + response.message.message);
                    } else {
                        frappe.msgprint(__('Site creation succeeded: ') + response.message.message);
                    }
                }
            });
        });
        // Add similar button for install_app...
    },
});
