import React from "react";

export const Footer = () => {
	return (
		<footer className="navbar fixed-bottom text-black footer">
			<div className="container  justify-content-center">
				<span>
					!ProBike <b>{new Date().getFullYear()}</b>
				</span>
			</div>
		</footer>
	);
};