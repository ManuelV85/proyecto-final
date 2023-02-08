

import React, { useEffect, useState } from "react";

const initialForm = {
	id: null,
	name: "",
	phone: "",
};

export const ContactForm = ({
	addContact,
	updateContact,
	dataToEdit,
	setDataToEdit,
}) => {
	const [form, setForm] = useState(initialForm);

	useEffect(() => {
		if (dataToEdit) {
			setForm(dataToEdit);
		} else {
			setForm(initialForm);
		}
	}, [dataToEdit]);

	const handleChange = e => {
		setForm({
			...form,
			[e.target.name]: e.target.value,
		});
	};

	const handleSubmit = e => {
		e.preventDefault();
		//* validation inputs not null
		if (
			form.name.trim().length > 2 ||
			form.phone.trim().length > 2
		) {
			//* validation add or update
			if (form.id === null) {
				addContact(form);
			} else {
				updateContact(form);
			}
			handleReset();
		}
	};

	const handleReset = () => {
		setForm(initialForm);
		setDataToEdit(null);
	};
	return (
		<div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
			<form onSubmit={handleSubmit}>
				<div className="form-floating mb-3">
					<input
						type="text"
						className="form-controll"
						id="name"
						name="name"
						placeholder="Nombre"
						autoComplete="off"
						onChange={handleChange}
						value={form.name}
					/>
					<label htmlFor="name"></label>
				</div>
				<div className="form-floating mb-3">
					<input
						type="tel"
						className="form-controll"
						id="phone"
						name="phone"
						placeholder="telefono"
						autoComplete="off"
						onChange={handleChange}
						value={form.phone}
					/>
					<label htmlFor="phone"></label>
				</div>

				<div className="mb-3 row">
					<div className="col-sm-12">
						{dataToEdit != null ? (
							<button
								type="submit"
								className="btn btn-darkk "
							>
								 Guardar datos editados
							</button>
						) : (
							<button
								type="submit"
								
								className="btn btn-darkk "
							>
								 Agregar
							</button>
						)}
					</div>
				</div>
			</form>
		</div>
	);
};