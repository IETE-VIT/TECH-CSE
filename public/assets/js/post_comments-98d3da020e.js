class PostComments{constructor(e){this.postId=e,this.postContainer=$(`#post-${e}`),this.newCommentForm=$(`#post-${e}-comments-form`),this.createComment(e);let t=this;$(" .delete-comment-button",this.postContainer).each((function(){t.deleteComment($(this))}))}createComment(e){let t=this;this.newCommentForm.submit((function(o){o.preventDefault();$.ajax({type:"post",url:"/users/commentcreate",data:$(this).serialize(),success:function(o){let n=t.newCommentDom(o.data.comment);$(`#post-comments-${e}`).prepend(n),t.deleteComment($(" .delete-comment-button",n)),new Noty({theme:"relax",text:"Comment published!",type:"success",layout:"topRight",timeout:1500}).show()},error:function(e){console.log(e.responseText)}})}))}newCommentDom(e){return $(`<div class="comment-box" id="comment-${e._id}">\n    <div>${e.content}</div>\n    <small>${e.user.name}</small>\n      <small><a class="delete-comment" href="/users/deletecomment/${e._id}">Delete comment</a></small>\n    \n    </div>`)}deleteComment(e){$(e).click((function(t){t.preventDefault(),$.ajax({type:"get",url:$(e).prop("href"),success:function(e){$(`#comment-${e.data.comment_id}`).remove(),new Noty({theme:"relax",text:"Comment Deleted",type:"success",layout:"topRight",timeout:1500}).show()},error:function(e){console.log(e.responseText)}})}))}}