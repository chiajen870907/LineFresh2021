var userId = "";
var displayName = "";
var pictureUrl = "";

function initializeLiff(myLiffId) {
    liff.init({
        liffId: myLiffId,
    })
        .then(() => {
            initializeApp();
            // initIdentity();

        })
        .catch(err => {
            console.log(err);
        });
}

function initializeApp() {
    // check if the user is logged in/out, and disable inappropriate button
    if (!liff.isLoggedIn()) {
        liff.login();
    } else {
        liff.getProfile()
            .then(profile => {
                userId = profile.userId;
                displayName = profile.displayName;
                pictureUrl = profile.pictureUrl;
                $("#user-image").attr("src", pictureUrl);
                $('#member-name').html(displayName + '，您好'); //赋值

            })
            .catch(err => {
                console.log(err);
            });
    }
}

initializeLiff('1656487192-GDz8ZxYQ');

