# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import CasperMessage_pb2 as CasperMessage__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DeployServiceStub(object):
  """--------- DeployService  --------
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.DoDeploy = channel.unary_unary(
        '/io.casperlabs.casper.protocol.DeployService/DoDeploy',
        request_serializer=CasperMessage__pb2.DeployData.SerializeToString,
        response_deserializer=CasperMessage__pb2.DeployServiceResponse.FromString,
        )
    self.createBlock = channel.unary_unary(
        '/io.casperlabs.casper.protocol.DeployService/createBlock',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=CasperMessage__pb2.DeployServiceResponse.FromString,
        )
    self.showBlock = channel.unary_unary(
        '/io.casperlabs.casper.protocol.DeployService/showBlock',
        request_serializer=CasperMessage__pb2.BlockQuery.SerializeToString,
        response_deserializer=CasperMessage__pb2.BlockQueryResponse.FromString,
        )
    self.visualizeDag = channel.unary_unary(
        '/io.casperlabs.casper.protocol.DeployService/visualizeDag',
        request_serializer=CasperMessage__pb2.VisualizeDagQuery.SerializeToString,
        response_deserializer=CasperMessage__pb2.VisualizeBlocksResponse.FromString,
        )
    self.showMainChain = channel.unary_stream(
        '/io.casperlabs.casper.protocol.DeployService/showMainChain',
        request_serializer=CasperMessage__pb2.BlocksQuery.SerializeToString,
        response_deserializer=CasperMessage__pb2.BlockInfoWithoutTuplespace.FromString,
        )
    self.showBlocks = channel.unary_stream(
        '/io.casperlabs.casper.protocol.DeployService/showBlocks',
        request_serializer=CasperMessage__pb2.BlocksQuery.SerializeToString,
        response_deserializer=CasperMessage__pb2.BlockInfoWithoutTuplespace.FromString,
        )
    self.findBlockWithDeploy = channel.unary_unary(
        '/io.casperlabs.casper.protocol.DeployService/findBlockWithDeploy',
        request_serializer=CasperMessage__pb2.FindDeployInBlockQuery.SerializeToString,
        response_deserializer=CasperMessage__pb2.BlockQueryResponse.FromString,
        )
    self.queryState = channel.unary_unary(
        '/io.casperlabs.casper.protocol.DeployService/queryState',
        request_serializer=CasperMessage__pb2.QueryStateRequest.SerializeToString,
        response_deserializer=CasperMessage__pb2.QueryStateResponse.FromString,
        )


class DeployServiceServicer(object):
  """--------- DeployService  --------
  """

  def DoDeploy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def createBlock(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def showBlock(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def visualizeDag(self, request, context):
    """Get dag
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def showMainChain(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def showBlocks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def findBlockWithDeploy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def queryState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DeployServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'DoDeploy': grpc.unary_unary_rpc_method_handler(
          servicer.DoDeploy,
          request_deserializer=CasperMessage__pb2.DeployData.FromString,
          response_serializer=CasperMessage__pb2.DeployServiceResponse.SerializeToString,
      ),
      'createBlock': grpc.unary_unary_rpc_method_handler(
          servicer.createBlock,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=CasperMessage__pb2.DeployServiceResponse.SerializeToString,
      ),
      'showBlock': grpc.unary_unary_rpc_method_handler(
          servicer.showBlock,
          request_deserializer=CasperMessage__pb2.BlockQuery.FromString,
          response_serializer=CasperMessage__pb2.BlockQueryResponse.SerializeToString,
      ),
      'visualizeDag': grpc.unary_unary_rpc_method_handler(
          servicer.visualizeDag,
          request_deserializer=CasperMessage__pb2.VisualizeDagQuery.FromString,
          response_serializer=CasperMessage__pb2.VisualizeBlocksResponse.SerializeToString,
      ),
      'showMainChain': grpc.unary_stream_rpc_method_handler(
          servicer.showMainChain,
          request_deserializer=CasperMessage__pb2.BlocksQuery.FromString,
          response_serializer=CasperMessage__pb2.BlockInfoWithoutTuplespace.SerializeToString,
      ),
      'showBlocks': grpc.unary_stream_rpc_method_handler(
          servicer.showBlocks,
          request_deserializer=CasperMessage__pb2.BlocksQuery.FromString,
          response_serializer=CasperMessage__pb2.BlockInfoWithoutTuplespace.SerializeToString,
      ),
      'findBlockWithDeploy': grpc.unary_unary_rpc_method_handler(
          servicer.findBlockWithDeploy,
          request_deserializer=CasperMessage__pb2.FindDeployInBlockQuery.FromString,
          response_serializer=CasperMessage__pb2.BlockQueryResponse.SerializeToString,
      ),
      'queryState': grpc.unary_unary_rpc_method_handler(
          servicer.queryState,
          request_deserializer=CasperMessage__pb2.QueryStateRequest.FromString,
          response_serializer=CasperMessage__pb2.QueryStateResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'io.casperlabs.casper.protocol.DeployService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
