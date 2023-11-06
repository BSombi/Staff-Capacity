// Copyright (c) 2023, IPC and contributors
// For license information, please see license.txt

frappe.ui.form.on("Employee", {
	refresh(frm) {
        frm.add_custom_button("Create Job Description", () => {
            let dialog = new frappe.ui.Dialog({
                title: "Select Job Title",
                fields: [
                    {
                        fieldtype: "Link",
                        fieldname: "job_title",
                        label: "Job Title",
                        options: "Job Title",
                    },
                ],
                primary_action_label: "Create Job Description",
                primary_action: (data) => {
                    console.log(data);
                    let { job_title } = data;

                    frappe.new_doc("Job Description", {

                        job_title: job_title
                    });
                },
            });

            dialog.show();
        });

        frm.add_custom_button("Create Psychometrics", () => {
            let dialog = new frappe.ui.Dialog({
                title: "Select Employee Name",
                fields: [
                    {
                        fieldtype: "Link",
                        fieldname: "employee_name",
                        label: "For Employee",
                        options: "Employee",
                    },
                ],
                primary_action_label: "Create Psychometrics",
                primary_action: (data) => {
                    console.log(data);
                    let { employee_name } = data;

                    frappe.new_doc("Employee Psychometrics", {
                        employee_name: frm.doc.employee_name,
                        employee_grade: frm.doc.employee_grade,
                        department: frm.doc.department,
                        job_title: frm.doc.job_title,
                        employee: employee_name,
                    });
                },
            });

            dialog.show();
        });
    

	},

	},
);

