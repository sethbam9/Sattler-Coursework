document.addEventListener('DOMContentLoaded', function() {


    document.querySelectorAll('.edit').forEach(btn => {

        btn.addEventListener('click', function() {


            //alert(btn.dataset.vehicle);

            const vehicleId = btn.dataset.vehicle;

            const description = document.querySelector(`.description[data-vehicle="${vehicleId}"]`)

            description.innerHTML = 'Flushed description!'

        })


        // if save clicked

        // fetch('/udpate_post')
        // {

        //     'postText':description.innerHTML;

        // }).then(

        //     //plug in the response value into description
        // )

    })
})
