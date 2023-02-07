import emailjs from "@emailjs/browser";

export const sendEmail = (params) => {
  console.log(params);
  const serviceId = process.env.SERVICE_ID;
  const templateId = process.env.TEMPLATE_ID;
  const key = process.env.KEY;
  console.log(serviceId);
  console.log(templateId);
  console.log(key);
  let templateIdtemp = params.templateId != null ? params.templateId:templateId
  
  const templateParams = {
    from_name: "iProBikeTEAM",
    to_email: params.to_email,
    to_name: params.to_name,
    to_link: params.to_link,
  };
  emailjs.send(serviceId, templateIdtemp, templateParams, key).then(
    (result) => {
      console.log(result.text);
    },
    (error) => {
      console.log(error.text);
    }
  );
};
