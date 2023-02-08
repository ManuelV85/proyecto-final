import React from "react";



export const ContactInfo = ({
	contact,
	setDataToEdit,
	deleteContact,
}) => {
	let { id, name, phone } = contact;
	return (
		<div className="p-2">
			<div role="alert" className="alert-info ">
				<div className="d-flex justify-content-between align-items-center">
					<div className="datos">
						<h5> {name}</h5>
						<h6> {phone}</h6>
					</div>
					<div className="losbuton">
						<button
							type="button"
							className="btn btn-outline-success bt-sm mx-3"
							onClick={() => setDataToEdit(contact)}
						>
							Editar
						</button>
						<button
							type="button"
							className="btn btn-outline-danger bt-sm mx-3"
							onClick={() => deleteContact(id)}
						>
							Borrar
						</button>
					</div>
				</div>
			</div>
		</div>
	);
};