'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
    constructor(props) {
        super(props);
        this.state = { liked: false };
    }

    render() {
        if (this.state.liked) {

            document.querySelectorAll('.my').forEach(myContainer => {
                const element = e('b', null, 'Ничего нет');
                ReactDOM.render(
                    element,
                    myContainer
                );
            });

            return 'You liked comment number ' + this.props.commentID;
            
        };

        return e(
            'button',
            { onClick: () => this.setState({ liked: true}) },
            'Like'
        );
    }
}

document.querySelectorAll('.like_button_container').forEach(domContainer => {
    const commentID = parseInt(domContainer.dataset.commentid);
    ReactDOM.render(
        e(LikeButton, { commentID: commentID }),
        domContainer
    );
});