import aws_cdk as core
import aws_cdk.assertions as assertions

from el_blog_cdk.el_blog_cdk_stack import ElBlogCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in el_blog_cdk/el_blog_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ElBlogCdkStack(app, "el-blog-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
