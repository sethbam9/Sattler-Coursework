document.addEventListener('DOMContentLoaded', function() {

    document.querySelectorAll('#edit-btn').forEach(btn => {

        btn.addEventListener('click', function() {

            const postId = btn.dataset.post;

            const description = document.querySelector(`#post-content[data-post="${postId}"]`)

            description.innerHTML = 'Flushed content!'

        })


        if save clicked

        fetch('/udpate_post')
        {

            'postText':description.innerHTML;

        }).then(

            //plug in the response value into description
        )

    })
})
