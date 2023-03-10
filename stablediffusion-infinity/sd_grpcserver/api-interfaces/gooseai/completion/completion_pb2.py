# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: completion.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63ompletion.proto\x12\x07gooseai\"!\n\x05Token\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\r\"(\n\x06Tokens\x12\x1e\n\x06tokens\x18\x01 \x03(\x0b\x32\x0e.gooseai.Token\"E\n\x06Prompt\x12\x0e\n\x04text\x18\x01 \x01(\tH\x00\x12!\n\x06tokens\x18\x02 \x01(\x0b\x32\x0f.gooseai.TokensH\x00\x42\x08\n\x06prompt\":\n\tLogitBias\x12\x1f\n\x06tokens\x18\x01 \x01(\x0b\x32\x0f.gooseai.Tokens\x12\x0c\n\x04\x62ias\x18\x02 \x01(\x01\"1\n\x0bLogitBiases\x12\"\n\x06\x62iases\x18\x01 \x03(\x0b\x32\x12.gooseai.LogitBias\"\xbb\x02\n\x0f\x46requencyParams\x12\x1d\n\x10presence_penalty\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12\x1e\n\x11\x66requency_penalty\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12\x1f\n\x12repetition_penalty\x18\x03 \x01(\x01H\x02\x88\x01\x01\x12%\n\x18repetition_penalty_slope\x18\x04 \x01(\x01H\x03\x88\x01\x01\x12%\n\x18repetition_penalty_range\x18\x05 \x01(\rH\x04\x88\x01\x01\x42\x13\n\x11_presence_penaltyB\x14\n\x12_frequency_penaltyB\x15\n\x13_repetition_penaltyB\x1b\n\x19_repetition_penalty_slopeB\x1b\n\x19_repetition_penalty_range\"\x9a\x02\n\x0eSamplingParams\x12&\n\x05order\x18\x01 \x03(\x0e\x32\x17.gooseai.SamplingMethod\x12\x18\n\x0btemperature\x18\x02 \x01(\x01H\x00\x88\x01\x01\x12\x12\n\x05top_p\x18\x03 \x01(\x01H\x01\x88\x01\x01\x12\x12\n\x05top_k\x18\x04 \x01(\rH\x02\x88\x01\x01\x12\x1f\n\x12tail_free_sampling\x18\x05 \x01(\x01H\x03\x88\x01\x01\x12\x16\n\ttypical_p\x18\x06 \x01(\x01H\x04\x88\x01\x01\x12\x12\n\x05top_a\x18\x07 \x01(\x01H\x05\x88\x01\x01\x42\x0e\n\x0c_temperatureB\x08\n\x06_top_pB\x08\n\x06_top_kB\x15\n\x13_tail_free_samplingB\x0c\n\n_typical_pB\x08\n\x06_top_a\"\xe4\x01\n\x0bModelParams\x12\x35\n\x0fsampling_params\x18\x01 \x01(\x0b\x32\x17.gooseai.SamplingParamsH\x00\x88\x01\x01\x12\x37\n\x10\x66requency_params\x18\x02 \x01(\x0b\x32\x18.gooseai.FrequencyParamsH\x01\x88\x01\x01\x12-\n\nlogit_bias\x18\x03 \x01(\x0b\x32\x14.gooseai.LogitBiasesH\x02\x88\x01\x01\x42\x12\n\x10_sampling_paramsB\x13\n\x11_frequency_paramsB\r\n\x0b_logit_bias\"$\n\x04\x45\x63ho\x12\x12\n\x05index\x18\x01 \x01(\x05H\x00\x88\x01\x01\x42\x08\n\x06_index\"*\n\x0fModuleEmbedding\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\"C\n\x06Tensor\x12\x1d\n\x03typ\x18\x01 \x01(\x0e\x32\x10.gooseai.NumType\x12\x0c\n\x04\x64ims\x18\x02 \x03(\r\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"~\n\tEmbedding\x12\x1e\n\x03raw\x18\x01 \x01(\x0b\x32\x0f.gooseai.TensorH\x00\x12*\n\x06module\x18\x02 \x01(\x0b\x32\x18.gooseai.ModuleEmbeddingH\x00\x12\x10\n\x03pos\x18\x03 \x01(\rH\x01\x88\x01\x01\x42\x0b\n\tembeddingB\x06\n\x04_pos\"\x98\x02\n\x0c\x45ngineParams\x12\x17\n\nmax_tokens\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x18\n\x0b\x63ompletions\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x15\n\x08logprobs\x18\x03 \x01(\rH\x02\x88\x01\x01\x12 \n\x04\x65\x63ho\x18\x04 \x01(\x0b\x32\r.gooseai.EchoH\x03\x88\x01\x01\x12\x14\n\x07\x62\x65st_of\x18\x05 \x01(\rH\x04\x88\x01\x01\x12\x1d\n\x04stop\x18\x06 \x03(\x0b\x32\x0f.gooseai.Prompt\x12\x17\n\nmin_tokens\x18\x07 \x01(\rH\x05\x88\x01\x01\x42\r\n\x0b_max_tokensB\x0e\n\x0c_completionsB\x0b\n\t_logprobsB\x07\n\x05_echoB\n\n\x08_best_ofB\r\n\x0b_min_tokens\"3\n\x0bRequestMeta\x12\x16\n\tstreaming\x18\x01 \x01(\x08H\x00\x88\x01\x01\x42\x0c\n\n_streaming\"\xf8\x02\n\x07Request\x12\x11\n\tengine_id\x18\x01 \x01(\t\x12\x1f\n\x06prompt\x18\x02 \x03(\x0b\x32\x0f.gooseai.Prompt\x12/\n\x0cmodel_params\x18\x03 \x01(\x0b\x32\x14.gooseai.ModelParamsH\x00\x88\x01\x01\x12\x31\n\rengine_params\x18\x04 \x01(\x0b\x32\x15.gooseai.EngineParamsH\x01\x88\x01\x01\x12\x17\n\nrequest_id\x18\x05 \x01(\tH\x02\x88\x01\x01\x12&\n\nembeddings\x18\x06 \x03(\x0b\x32\x12.gooseai.Embedding\x12\x1c\n\x0forigin_received\x18\x07 \x01(\x04H\x03\x88\x01\x01\x12\'\n\x04meta\x18\x08 \x01(\x0b\x32\x14.gooseai.RequestMetaH\x04\x88\x01\x01\x42\x0f\n\r_model_paramsB\x10\n\x0e_engine_paramsB\r\n\x0b_request_idB\x12\n\x10_origin_receivedB\x07\n\x05_meta\"z\n\x07LogProb\x12\x1d\n\x05token\x18\x01 \x01(\x0b\x32\x0e.gooseai.Token\x12\x14\n\x07logprob\x18\x02 \x01(\x01H\x00\x88\x01\x01\x12\x1b\n\x0elogprob_before\x18\x03 \x01(\x01H\x01\x88\x01\x01\x42\n\n\x08_logprobB\x11\n\x0f_logprob_before\"3\n\rTokenLogProbs\x12\"\n\x08logprobs\x18\x01 \x03(\x0b\x32\x10.gooseai.LogProb\"\x98\x01\n\x08LogProbs\x12&\n\x06tokens\x18\x01 \x01(\x0b\x32\x16.gooseai.TokenLogProbs\x12\x13\n\x0btext_offset\x18\x02 \x03(\r\x12#\n\x03top\x18\x03 \x03(\x0b\x32\x16.gooseai.TokenLogProbs\x12*\n\ntop_before\x18\x04 \x03(\x0b\x32\x16.gooseai.TokenLogProbs\"\xa2\x01\n\nCompletion\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\r\x12#\n\x08logprobs\x18\x03 \x01(\x0b\x32\x11.gooseai.LogProbs\x12,\n\rfinish_reason\x18\x04 \x01(\x0e\x32\x15.gooseai.FinishReason\x12\x13\n\x0btoken_index\x18\x05 \x01(\r\x12\x0f\n\x07started\x18\x06 \x01(\x04\"n\n\nAnswerMeta\x12\x13\n\x06gpu_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06\x63pu_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07node_id\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\t\n\x07_gpu_idB\t\n\x07_cpu_idB\n\n\x08_node_id\"\xd6\x01\n\x06\x41nswer\x12\x11\n\tanswer_id\x18\x01 \x01(\t\x12\x0f\n\x07\x63reated\x18\x02 \x01(\x04\x12\r\n\x05model\x18\x03 \x01(\t\x12$\n\x07\x63hoices\x18\x04 \x03(\x0b\x32\x13.gooseai.Completion\x12\x17\n\nrequest_id\x18\x05 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\x12inference_received\x18\x06 \x01(\x04\x12&\n\x04meta\x18\x07 \x01(\x0b\x32\x13.gooseai.AnswerMetaH\x01\x88\x01\x01\x42\r\n\x0b_request_idB\x07\n\x05_meta*9\n\x0c\x46inishReason\x12\x08\n\x04NULL\x10\x00\x12\n\n\x06LENGTH\x10\x01\x12\x08\n\x04STOP\x10\x02\x12\t\n\x05\x45RROR\x10\x03*d\n\x0eSamplingMethod\x12\x08\n\x04NONE\x10\x00\x12\x0f\n\x0bTEMPERATURE\x10\x01\x12\t\n\x05TOP_K\x10\x02\x12\t\n\x05TOP_P\x10\x03\x12\x07\n\x03TFS\x10\x04\x12\t\n\x05TOP_A\x10\x05\x12\r\n\tTYPICAL_P\x10\x06*\'\n\x07NumType\x12\x08\n\x04\x46P16\x10\x00\x12\x08\n\x04\x46P32\x10\x01\x12\x08\n\x04\x42\x46\x31\x36\x10\x02\x32H\n\x11\x43ompletionService\x12\x33\n\nCompletion\x12\x10.gooseai.Request\x1a\x0f.gooseai.Answer\"\x00\x30\x01\x42\x0fZ\r./;completionb\x06proto3')

_FINISHREASON = DESCRIPTOR.enum_types_by_name['FinishReason']
FinishReason = enum_type_wrapper.EnumTypeWrapper(_FINISHREASON)
_SAMPLINGMETHOD = DESCRIPTOR.enum_types_by_name['SamplingMethod']
SamplingMethod = enum_type_wrapper.EnumTypeWrapper(_SAMPLINGMETHOD)
_NUMTYPE = DESCRIPTOR.enum_types_by_name['NumType']
NumType = enum_type_wrapper.EnumTypeWrapper(_NUMTYPE)
NULL = 0
LENGTH = 1
STOP = 2
ERROR = 3
NONE = 0
TEMPERATURE = 1
TOP_K = 2
TOP_P = 3
TFS = 4
TOP_A = 5
TYPICAL_P = 6
FP16 = 0
FP32 = 1
BF16 = 2


_TOKEN = DESCRIPTOR.message_types_by_name['Token']
_TOKENS = DESCRIPTOR.message_types_by_name['Tokens']
_PROMPT = DESCRIPTOR.message_types_by_name['Prompt']
_LOGITBIAS = DESCRIPTOR.message_types_by_name['LogitBias']
_LOGITBIASES = DESCRIPTOR.message_types_by_name['LogitBiases']
_FREQUENCYPARAMS = DESCRIPTOR.message_types_by_name['FrequencyParams']
_SAMPLINGPARAMS = DESCRIPTOR.message_types_by_name['SamplingParams']
_MODELPARAMS = DESCRIPTOR.message_types_by_name['ModelParams']
_ECHO = DESCRIPTOR.message_types_by_name['Echo']
_MODULEEMBEDDING = DESCRIPTOR.message_types_by_name['ModuleEmbedding']
_TENSOR = DESCRIPTOR.message_types_by_name['Tensor']
_EMBEDDING = DESCRIPTOR.message_types_by_name['Embedding']
_ENGINEPARAMS = DESCRIPTOR.message_types_by_name['EngineParams']
_REQUESTMETA = DESCRIPTOR.message_types_by_name['RequestMeta']
_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_LOGPROB = DESCRIPTOR.message_types_by_name['LogProb']
_TOKENLOGPROBS = DESCRIPTOR.message_types_by_name['TokenLogProbs']
_LOGPROBS = DESCRIPTOR.message_types_by_name['LogProbs']
_COMPLETION = DESCRIPTOR.message_types_by_name['Completion']
_ANSWERMETA = DESCRIPTOR.message_types_by_name['AnswerMeta']
_ANSWER = DESCRIPTOR.message_types_by_name['Answer']
Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), {
  'DESCRIPTOR' : _TOKEN,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Token)
  })
_sym_db.RegisterMessage(Token)

Tokens = _reflection.GeneratedProtocolMessageType('Tokens', (_message.Message,), {
  'DESCRIPTOR' : _TOKENS,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Tokens)
  })
_sym_db.RegisterMessage(Tokens)

Prompt = _reflection.GeneratedProtocolMessageType('Prompt', (_message.Message,), {
  'DESCRIPTOR' : _PROMPT,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Prompt)
  })
_sym_db.RegisterMessage(Prompt)

LogitBias = _reflection.GeneratedProtocolMessageType('LogitBias', (_message.Message,), {
  'DESCRIPTOR' : _LOGITBIAS,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.LogitBias)
  })
_sym_db.RegisterMessage(LogitBias)

LogitBiases = _reflection.GeneratedProtocolMessageType('LogitBiases', (_message.Message,), {
  'DESCRIPTOR' : _LOGITBIASES,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.LogitBiases)
  })
_sym_db.RegisterMessage(LogitBiases)

FrequencyParams = _reflection.GeneratedProtocolMessageType('FrequencyParams', (_message.Message,), {
  'DESCRIPTOR' : _FREQUENCYPARAMS,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.FrequencyParams)
  })
_sym_db.RegisterMessage(FrequencyParams)

SamplingParams = _reflection.GeneratedProtocolMessageType('SamplingParams', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLINGPARAMS,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.SamplingParams)
  })
_sym_db.RegisterMessage(SamplingParams)

ModelParams = _reflection.GeneratedProtocolMessageType('ModelParams', (_message.Message,), {
  'DESCRIPTOR' : _MODELPARAMS,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ModelParams)
  })
_sym_db.RegisterMessage(ModelParams)

Echo = _reflection.GeneratedProtocolMessageType('Echo', (_message.Message,), {
  'DESCRIPTOR' : _ECHO,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Echo)
  })
_sym_db.RegisterMessage(Echo)

ModuleEmbedding = _reflection.GeneratedProtocolMessageType('ModuleEmbedding', (_message.Message,), {
  'DESCRIPTOR' : _MODULEEMBEDDING,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ModuleEmbedding)
  })
_sym_db.RegisterMessage(ModuleEmbedding)

Tensor = _reflection.GeneratedProtocolMessageType('Tensor', (_message.Message,), {
  'DESCRIPTOR' : _TENSOR,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Tensor)
  })
_sym_db.RegisterMessage(Tensor)

Embedding = _reflection.GeneratedProtocolMessageType('Embedding', (_message.Message,), {
  'DESCRIPTOR' : _EMBEDDING,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Embedding)
  })
_sym_db.RegisterMessage(Embedding)

EngineParams = _reflection.GeneratedProtocolMessageType('EngineParams', (_message.Message,), {
  'DESCRIPTOR' : _ENGINEPARAMS,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.EngineParams)
  })
_sym_db.RegisterMessage(EngineParams)

RequestMeta = _reflection.GeneratedProtocolMessageType('RequestMeta', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTMETA,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.RequestMeta)
  })
_sym_db.RegisterMessage(RequestMeta)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Request)
  })
_sym_db.RegisterMessage(Request)

LogProb = _reflection.GeneratedProtocolMessageType('LogProb', (_message.Message,), {
  'DESCRIPTOR' : _LOGPROB,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.LogProb)
  })
_sym_db.RegisterMessage(LogProb)

TokenLogProbs = _reflection.GeneratedProtocolMessageType('TokenLogProbs', (_message.Message,), {
  'DESCRIPTOR' : _TOKENLOGPROBS,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TokenLogProbs)
  })
_sym_db.RegisterMessage(TokenLogProbs)

LogProbs = _reflection.GeneratedProtocolMessageType('LogProbs', (_message.Message,), {
  'DESCRIPTOR' : _LOGPROBS,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.LogProbs)
  })
_sym_db.RegisterMessage(LogProbs)

Completion = _reflection.GeneratedProtocolMessageType('Completion', (_message.Message,), {
  'DESCRIPTOR' : _COMPLETION,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Completion)
  })
_sym_db.RegisterMessage(Completion)

AnswerMeta = _reflection.GeneratedProtocolMessageType('AnswerMeta', (_message.Message,), {
  'DESCRIPTOR' : _ANSWERMETA,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.AnswerMeta)
  })
_sym_db.RegisterMessage(AnswerMeta)

Answer = _reflection.GeneratedProtocolMessageType('Answer', (_message.Message,), {
  'DESCRIPTOR' : _ANSWER,
  '__module__' : 'completion_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Answer)
  })
_sym_db.RegisterMessage(Answer)

_COMPLETIONSERVICE = DESCRIPTOR.services_by_name['CompletionService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\r./;completion'
  _FINISHREASON._serialized_start=2942
  _FINISHREASON._serialized_end=2999
  _SAMPLINGMETHOD._serialized_start=3001
  _SAMPLINGMETHOD._serialized_end=3101
  _NUMTYPE._serialized_start=3103
  _NUMTYPE._serialized_end=3142
  _TOKEN._serialized_start=29
  _TOKEN._serialized_end=62
  _TOKENS._serialized_start=64
  _TOKENS._serialized_end=104
  _PROMPT._serialized_start=106
  _PROMPT._serialized_end=175
  _LOGITBIAS._serialized_start=177
  _LOGITBIAS._serialized_end=235
  _LOGITBIASES._serialized_start=237
  _LOGITBIASES._serialized_end=286
  _FREQUENCYPARAMS._serialized_start=289
  _FREQUENCYPARAMS._serialized_end=604
  _SAMPLINGPARAMS._serialized_start=607
  _SAMPLINGPARAMS._serialized_end=889
  _MODELPARAMS._serialized_start=892
  _MODELPARAMS._serialized_end=1120
  _ECHO._serialized_start=1122
  _ECHO._serialized_end=1158
  _MODULEEMBEDDING._serialized_start=1160
  _MODULEEMBEDDING._serialized_end=1202
  _TENSOR._serialized_start=1204
  _TENSOR._serialized_end=1271
  _EMBEDDING._serialized_start=1273
  _EMBEDDING._serialized_end=1399
  _ENGINEPARAMS._serialized_start=1402
  _ENGINEPARAMS._serialized_end=1682
  _REQUESTMETA._serialized_start=1684
  _REQUESTMETA._serialized_end=1735
  _REQUEST._serialized_start=1738
  _REQUEST._serialized_end=2114
  _LOGPROB._serialized_start=2116
  _LOGPROB._serialized_end=2238
  _TOKENLOGPROBS._serialized_start=2240
  _TOKENLOGPROBS._serialized_end=2291
  _LOGPROBS._serialized_start=2294
  _LOGPROBS._serialized_end=2446
  _COMPLETION._serialized_start=2449
  _COMPLETION._serialized_end=2611
  _ANSWERMETA._serialized_start=2613
  _ANSWERMETA._serialized_end=2723
  _ANSWER._serialized_start=2726
  _ANSWER._serialized_end=2940
  _COMPLETIONSERVICE._serialized_start=3144
  _COMPLETIONSERVICE._serialized_end=3216
# @@protoc_insertion_point(module_scope)
